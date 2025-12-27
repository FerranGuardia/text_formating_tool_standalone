import os
import pytest
from src.queue_item import QueueItem


@pytest.fixture
def valid_paths(tmp_path):
    input_folder = tmp_path / "input"
    input_folder.mkdir()

    output_folder = tmp_path / "out"
    output_folder.mkdir()

    return str(input_folder), str(output_folder)

# --- Test for behaviour of the class. ---


def test_queue_item_missing_file(tmp_path):

    output = tmp_path / "out"
    output.mkdir()

    with pytest.raises(NotADirectoryError):
        QueueItem("does_not_exist", str(output))


def test_queue_item_missing_output_folder(tmp_path):

    input_folder = tmp_path / "input"
    input_folder.mkdir()

    with pytest.raises(NotADirectoryError):
        QueueItem(str(input_folder), "missing_folder")


def test_queue_item_valid(tmp_path):

    input_folder = tmp_path / "input"
    input_folder.mkdir()

    output = tmp_path / "out"
    output.mkdir()

    item = QueueItem(str(input_folder), str(output))

    assert item.input_folder == str(input_folder)
    assert item.output_folder == str(output)
    assert item.status == "Pending"
    assert item.progress == 0

# --- Test for method start ---


def test_start_queue_status_to_processing(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)

    item.start()
    assert item.status == "Processing"


def test_start_queue_status_not_pending(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)

    item.status = ""  # invalid state

    with pytest.raises(RuntimeError):
        item.start()

# --- Test for method pause ---


def test_pausing_from_processing(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Processing"

    item.pause()
    assert item.status == "Paused"


def test_pausing_from_any(valid_paths):
     
    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = ""
    
    with pytest.raises(RuntimeError):
      item.pause()


def test_pausing_from_paused(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Paused"

    with pytest.raises(RuntimeError):
        item.pause()


def test_pausing_from_pending(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Pending"

    with pytest.raises(RuntimeError):
        item.pause()


def test_pausing_from_completed(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Completed"

    with pytest.raises(RuntimeError):
        item.pause()

# --- Test for method resume --- 

def test_resuming_from_paused(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Paused"

    item.resume()
    assert item.status == "Processing"

def test_resuming_from_any(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = ""

    with pytest.raises(RuntimeError):
        item.resume()

def test_resuming_from_completed(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Completed"

    with pytest.raises(RuntimeError):
        item.resume()

def test_resuming_from_pending(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Pending"

    with pytest.raises(RuntimeError):
        item.resume()

def test_resuming_from_processing(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Processing"

    with pytest.raises(RuntimeError):
        item.resume()

# --- Tests for method complete --- 

def test_completing_from_processing(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Processing"

    item.complete()
    assert item.status == "Completed"

def test_completing_from_any(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = ""

    with pytest.raises(RuntimeError):
        item.complete()

def test_completing_from_pending(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Pending"

    with pytest.raises(RuntimeError):
        item.complete()

def test_completing_from_paused(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Paused"

    with pytest.raises(RuntimeError):
        item.complete()

def test_completing_from_complete(valid_paths):

    input_folder, output_folder = valid_paths
    item = QueueItem(input_folder, output_folder)
    item.status = "Completed"

    with pytest.raises(RuntimeError):
        item.complete()