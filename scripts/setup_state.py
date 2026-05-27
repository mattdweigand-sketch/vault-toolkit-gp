#!/usr/bin/env python3
"""Small setup-state helper for the GP Operating Toolkit."""

from argparse import ArgumentParser
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re


WORKFLOWS = [
    "diligence-evidence-map",
    "firm-memory-loop",
    "hold-sell-refi",
    "ic-pressure-test",
    "lp-narrative-and-issue-prep",
    "market-thesis-to-investment-box",
    "portfolio-intervention",
    "underwriting-backtest",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def shared_dir(root: Path) -> Path:
    return root / "_shared-config"


def session_path(root: Path) -> Path:
    return shared_dir(root) / "setup-session.json"


def session_lock_path(root: Path) -> Path:
    return shared_dir(root) / "setup-session.lock"


def progress_path(root: Path) -> Path:
    return shared_dir(root) / "setup-progress.md"


def firm_profile_path(root: Path) -> Path:
    return shared_dir(root) / "firm-profile.md"


def agents_path(root: Path) -> Path:
    return root / "AGENTS.md"


def setup_path(root: Path) -> Path:
    return root / "SETUP.md"


def default_session() -> dict:
    return {
        "version": 1,
        "current_phase": "orientation",
        "current_step": "firm_orientation",
        "firm_orientation": {},
        "value_triage": {},
        "selected_workflow": None,
        "current_question": None,
        "answers": {},
        "open_confirmations": [],
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }


def read_text(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def read_json(path: Path):
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


@contextmanager
def locked_session(root: Path):
    path = session_lock_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_file, fcntl.LOCK_UN)


def firm_profile_has_placeholders(root: Path) -> bool:
    text = read_text(firm_profile_path(root))
    return bool(re.search(r"\[[^\]]+\]", text))


def ag_bootstrap_is_stale(root: Path) -> bool:
    text = read_text(agents_path(root))
    return "## Where to go from here" in text and "setup-progress.md" in text


def firm_orientation_captured(session) -> bool:
    if not session:
        return False
    orientation = session.get("firm_orientation")
    return isinstance(orientation, dict) and bool(orientation)


def builder_questions_complete(session) -> bool:
    if not session:
        return False
    answers = session.get("answers")
    return isinstance(answers, dict) and answers.get("builder_questions_complete") is True


def setup_status(root: Path) -> dict:
    session = read_json(session_path(root))
    progress_exists = progress_path(root).is_file()
    stale_bootstrap = ag_bootstrap_is_stale(root)
    placeholders = firm_profile_has_placeholders(root)

    if progress_exists and not stale_bootstrap:
        state = "complete"
    elif (
        session
        and not progress_exists
        and firm_orientation_captured(session)
        and session.get("selected_workflow")
        and not builder_questions_complete(session)
    ):
        state = "ready_to_build"
    elif session and not progress_exists:
        state = "in_progress"
    elif not progress_exists and not session and placeholders:
        state = "not_started"
    else:
        state = "in_progress"

    return {
        "status": state,
        "setup_progress_exists": progress_exists,
        "setup_session_exists": session is not None,
        "firm_profile_has_placeholders": placeholders,
        "agents_bootstrap_is_stale": stale_bootstrap,
        "session_path": str(session_path(root)),
    }


def table_missing_items(text: str, items) -> list:
    missing = []
    for item in items:
        if item not in text:
            missing.append(item)
    return missing


def doctor(root: Path) -> dict:
    architectures = sorted(
        path.name
        for path in (root / "architectures").iterdir()
        if path.is_dir() and path.name != "_variants"
    ) if (root / "architectures").is_dir() else []
    builders = sorted(
        path.name.removesuffix("-builder.md")
        for path in (root / "skill-starters").glob("*-builder.md")
    ) if (root / "skill-starters").is_dir() else []
    constraints = sorted(
        path.name for path in (root / "constraints").glob("*.md")
    ) if (root / "constraints").is_dir() else []
    setup_text = read_text(setup_path(root))
    readme_text = read_text(root / "README.md")

    expected = set(WORKFLOWS)
    architecture_set = set(architectures)
    builder_set = set(builders)
    workspaces_dir = root / "workspaces"
    live_workspaces = [
        path for path in workspaces_dir.iterdir() if path.is_dir()
    ] if workspaces_dir.is_dir() else []

    return {
        **setup_status(root),
        "counts": {
            "architectures": len(architectures),
            "builders": len(builders),
            "constraints": len(constraints),
        },
        "registry": {
            "architectures_missing": sorted(expected - architecture_set),
            "architectures_extra": sorted(architecture_set - expected),
            "builders_missing": sorted(expected - builder_set),
            "builders_extra": sorted(builder_set - expected),
            "setup_table_missing": table_missing_items(setup_text, WORKFLOWS),
            "readme_missing": table_missing_items(readme_text, WORKFLOWS),
        },
        "open_items": [
            item for item, open_item in [
                ("setup-progress.md missing", not progress_path(root).is_file()),
                ("workspaces directory missing", not workspaces_dir.is_dir()),
                ("workspaces directory has no workspaces", workspaces_dir.is_dir() and not live_workspaces),
                ("firm-profile.md contains placeholders", firm_profile_has_placeholders(root)),
                ("AGENTS.md still has bootstrap text", ag_bootstrap_is_stale(root)),
            ] if open_item
        ],
    }


def set_dotted(payload: dict, dotted: str, value) -> None:
    target = payload
    parts = dotted.split(".")
    for part in parts[:-1]:
        current = target.get(part)
        if not isinstance(current, dict):
            current = {}
            target[part] = current
        target = current
    target[parts[-1]] = value


def parse_value(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def init_session(root: Path) -> dict:
    with locked_session(root):
        path = session_path(root)
        existing = read_json(path)
        if existing:
            existing["updated_at"] = now_iso()
            write_json(path, existing)
            return existing
        payload = default_session()
        write_json(path, payload)
        return payload


def record(root: Path, field: str, value: str) -> dict:
    with locked_session(root):
        payload = read_json(session_path(root)) or default_session()
        set_dotted(payload, field, parse_value(value))
        payload["updated_at"] = now_iso()
        write_json(session_path(root), payload)
        return payload


def clear_session(root: Path) -> dict:
    with locked_session(root):
        path = session_path(root)
        removed = path.is_file()
        if removed:
            path.unlink()
        return {"removed": removed, "session_path": str(path)}


def emit(payload: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, indent=2))
        return

    if "status" in payload:
        print(f"status: {payload['status']}")
    if "open_items" in payload:
        items = payload["open_items"]
        print("open_items: " + (", ".join(items) if items else "none"))
    if "counts" in payload:
        counts = payload["counts"]
        print(
            "counts: "
            f"{counts['architectures']} architectures, "
            f"{counts['builders']} builders, "
            f"{counts['constraints']} constraints"
        )
    if "session_path" in payload:
        print(f"session: {payload['session_path']}")
    if "removed" in payload:
        print(f"removed: {payload['removed']}")


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="GP Toolkit setup state helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("status", "doctor", "init-session", "clear-session"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--json", action="store_true")

    record_parser = subparsers.add_parser("record")
    record_parser.add_argument("--field", required=True)
    record_parser.add_argument("--value", required=True)
    record_parser.add_argument("--json", action="store_true")

    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = repo_root()

    if args.command == "status":
        emit(setup_status(root), args.json)
    elif args.command == "doctor":
        emit(doctor(root), args.json)
    elif args.command == "init-session":
        emit(init_session(root), args.json)
    elif args.command == "record":
        emit(record(root, args.field, args.value), args.json)
    elif args.command == "clear-session":
        emit(clear_session(root), args.json)
    return 0


raise SystemExit(main())
