import pytest
from src.queue_class import Queue
from src.queue_item import QueueItem

@pytest.fixture
def folders(tmp_path):

    input_folder = tmp_path / "book"
    input_folder.mkdir()

    output_folder = tmp_path /"out"
    output_folder.mkdir()

    return str(input_folder), str(output_folder)

#---Inizialization---

def test_queue_state():

    queue = Queue()
    assert queue.items == []
    assert queue.current_index is None

#---Method---


def test_add_item_adds_queueitem(folders):

    input_folder, output_folder = folders
    queue = Queue()
    item = queue.add_item(input_folder, output_folder)

    assert len(queue.items) == 1
    assert isinstance(item, QueueItem)
    assert queue.items[0] is item

def test_is_current_item_in_queue_none():
    queue = Queue()
    assert queue.current_item is None

