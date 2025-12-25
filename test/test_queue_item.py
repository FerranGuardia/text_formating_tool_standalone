import os
import pytest
from src.queue_item import QueueItem

def test_queue_item_missing_file(tmp_path):
    output = tmp_path / "out"
    output.mkdir()

    with pytest.raises(FileNotFoundError):
        QueueItem("does_not_exist.txt", str(output))

