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
        
# --- Start Item ---
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

def test_order_items_added(folders):

    input_folder, output_folder = folders
    queue = Queue()
    item1 = queue.add_item(input_folder, output_folder)
    item2 = queue.add_item(input_folder, output_folder)
    item3 = queue.add_item(input_folder, output_folder)

    assert len(queue.items) == 3
    assert queue.items[0] is item1
    assert queue.items[1] is item2
    assert queue.items[2] is item3

#---Remove Item---

#---validation---
def test_remove_item_negative_index(folders):
    input_folder, output_folder = folders
    queue = Queue()
    queue.add_item(input_folder, output_folder)

    with pytest.raises(IndexError):
        queue.remove_item(-1)

def test_remove_item_index_to_large(folders):
    input_folder, output_folder = folders
    queue = Queue()
    queue.add_item(input_folder, output_folder)

    with pytest.raises(IndexError):
        queue.remove_item(1)

def test_remove_item_empty_queue():
    queue = Queue()

    with pytest.raises(IndexError):
        queue.remove_item(0)


