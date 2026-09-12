import json
import re
from pathlib import Path

ENGLISH = re.compile(r"[A-Za-z]")
JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
REQUIRED_TEXT = ("title", "summary", "inference")
REQUIRED_LISTS = ("steps", "concepts", "observations")
OPTIONAL_TEXT = ("limitations",)
OPTIONAL_LISTS = ("parameters",)
ALLOWED_KEYS = {*REQUIRED_TEXT, *REQUIRED_LISTS, *OPTIONAL_TEXT, *OPTIONAL_LISTS}
INFERENCE_VALUES = {
    "training_outputs_only",
    "implementation_reviewed_against_provided_pairs",
}
FORBIDDEN_PHRASES = (
    "input fingerprint",
    "hash patch",
    "answer table",
    "the implementation applies the structural transform first",
    "brown 6",
    "orange 9",
)


def note_violations(root: Path) -> list[str]:
    failures: list[str] = []
    solutions = {path.stem for path in (root / "solutions").glob("????????.py")}
    notes = {path.stem: path for path in (root / "notes").glob("????????.json")}
    for task_id in sorted(solutions - set(notes)):
        failures.append(f"{task_id}: note is missing")
    for task_id in sorted(set(notes) - solutions):
        failures.append(f"{task_id}: note has no active solution")

    for task_id in sorted(solutions & set(notes)):
        try:
            note = json.loads(notes[task_id].read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{task_id}: invalid JSON: {exc}")
            continue
        extra_keys = sorted(set(note) - ALLOWED_KEYS)
        if extra_keys:
            failures.append(f"{task_id}: unsupported fields: {', '.join(extra_keys)}")
        for key in REQUIRED_TEXT:
            value = note.get(key)
            if not isinstance(value, str) or not value.strip():
                failures.append(f"{task_id}: {key} must be non-empty text")
            elif key != "inference" and (not ENGLISH.search(value) or JAPANESE.search(value)):
                failures.append(f"{task_id}: {key} must contain English-only prose")
        summary = note.get("summary")
        if isinstance(summary, str) and len(re.findall(r"[A-Za-z0-9]+", summary)) < 5:
            failures.append(f"{task_id}: summary is too vague to describe the transformation")
        for key in OPTIONAL_TEXT:
            value = note.get(key)
            if value is not None and (
                not isinstance(value, str) or not ENGLISH.search(value) or JAPANESE.search(value)
            ):
                failures.append(f"{task_id}: {key} must contain English-only prose")
        for key in (*REQUIRED_LISTS, *OPTIONAL_LISTS):
            value = note.get(key)
            required_missing = key in REQUIRED_LISTS and (not isinstance(value, list) or not value)
            malformed = value is not None and (
                not isinstance(value, list)
                or not value
                or not all(isinstance(item, str) and item.strip() for item in value)
            )
            if required_missing or malformed:
                failures.append(f"{task_id}: {key} must be a non-empty text list")
            elif isinstance(value, list) and (
                any(JAPANESE.search(item) for item in value)
                or (key != "concepts" and any(not ENGLISH.search(item) for item in value))
            ):
                failures.append(f"{task_id}: {key} must contain English-only prose")
        if note.get("inference") not in INFERENCE_VALUES:
            failures.append(f"{task_id}: inference is invalid")

        task_path = next(
            (
                root / "data" / split / f"{task_id}.json"
                for split in ("training", "evaluation")
                if (root / "data" / split / f"{task_id}.json").exists()
            ),
            None,
        )
        if task_path is None:
            failures.append(f"{task_id}: task data is missing")
        else:
            task = json.loads(task_path.read_text(encoding="utf-8"))
            if len(note.get("observations", [])) != len(task["train"]):
                failures.append(f"{task_id}: training observations are incomplete")
        serialized = json.dumps(note, ensure_ascii=False).lower()
        for phrase in FORBIDDEN_PHRASES:
            if phrase in serialized:
                failures.append(f"{task_id}: forbidden replay wording: {phrase}")
    return failures


def test_all_solution_notes_satisfy_contract() -> None:
    assert note_violations(Path(".")) == []
