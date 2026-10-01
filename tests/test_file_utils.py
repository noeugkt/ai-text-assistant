import pytest
from file_utils import read_text

def test_read_text_missing_file():
    with pytest.raises(FileNotFoundError):
        read_text("file_that_does_not_exist.txt")

def test_read_text(tmp_path):
    test_file = tmp_path/"test.txt"

    test_file.write_text(
        "Hello from the test file.",
        encoding="utf-8"
    )

    result = read_text(test_file)

    assert result == "Hello from the test file."
