import json
import tempfile
from pathlib import Path

from load_summary import load_requirements


def test_valid_json_returns_expected_list():
    expected_requirements = [
        {"id": "REQ-001", "text": "Validate user login", "status": "approved"},
        {"id": "REQ-002", "text": "Log admin actions", "status": "draft"},
    ]

    with tempfile.TemporaryDirectory() as directory:
        requirements_file = Path(directory) / "valid_requirements.json"

        with requirements_file.open("w", encoding="utf-8") as file:
            json.dump(expected_requirements, file)

        actual_requirements = load_requirements(requirements_file)

    assert actual_requirements == expected_requirements


def test_missing_file_raises_file_not_found_error():
    with tempfile.TemporaryDirectory() as directory:
        missing_file = Path(directory) / "does_not_exist.json"

        try:
            load_requirements(missing_file)
        except FileNotFoundError:
            pass
        else:
            raise AssertionError("Expected FileNotFoundError to be raised")


def test_invalid_json_raises_json_decode_error():
    with tempfile.TemporaryDirectory() as directory:
        invalid_file = Path(directory) / "invalid_requirements.json"
        invalid_file.write_text(
            '{"id": "REQ-001", broken JSON',
            encoding="utf-8"
        )

        try:
            load_requirements(invalid_file)
        except json.JSONDecodeError:
            pass
        else:
            raise AssertionError("Expected JSONDecodeError to be raised")


if __name__ == "__main__":
    test_valid_json_returns_expected_list()
    test_missing_file_raises_file_not_found_error()
    test_invalid_json_raises_json_decode_error()
    print("all tests passed")

