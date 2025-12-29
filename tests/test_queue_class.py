import pytest
from src.queue_class import Queue
from src.queue_item import QueueItem

@pytest.fixture
def queue_with_three_items(folders):
    input_folder, output_folder = folders
    queue = Queue()
    item1 = queue.add_item(input_folder, output_folder)
    item2 = queue.add_item(input_folder, output_folder)
    item3 = queue.add_item(input_folder, output_folder)
    return queue, item1, item2, item3

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

def test_order_items_added(queue_with_three_items):

    queue, item1, item2, item3 = queue_with_three_items

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

# Current Index Scenario Test
def test_remove_current_item_sets_current_index_to_none(queue_with_three_items):

    queue, item1, item2, item3 = queue_with_three_items

    queue.current_index = 1  
    removed = queue.remove_item(1)

    assert removed is item2
    assert queue.current_index is None  
    assert queue.items[1] is item3

def test_remove_item_before_current_decrements_current_index(queue_with_three_items):

    queue, item1, item2, item3 = queue_with_three_items

    queue.current_index = 2  
    removed = queue.remove_item(0)

    assert removed is item1
    assert queue.current_index == 1   
    assert queue.items[1] is item3

def test_remove_item_after_current_no_change(queue_with_three_items):

    queue, item1, item2, item3 = queue_with_three_items

    queue.current_index = 0  
    removed = queue.remove_item(2)

    assert removed is item3
    assert queue.current_index == 0   
    assert queue.items[0] is item1

def test_remove_item_when_current_index_is_none(folders):

    input_folder, output_folder = folders
    queue = Queue()
    item1 = queue.add_item(input_folder, output_folder)
    item2 = queue.add_item(input_folder, output_folder)
    
    removed = queue.remove_item(0)

    assert queue.items[0] is item2
    assert len(queue.items) == 1

# Functionality test
def test_remove_item_return_removed_item(folders):

    input_folder, output_folder = folders
    queue = Queue()
    item = queue.add_item(input_folder, output_folder)

    removed = queue.remove_item(0)

    assert removed is item
    assert len(queue.items) == 0

def test_remove_item_removes_from_list(folders):

    input_folder, output_folder = folders
    queue = Queue()
    item = queue.add_item(input_folder, output_folder)
    item2 = queue.add_item(input_folder, output_folder)

    queue.remove_item(0)

    assert len(queue.items) == 1
    assert queue.items[0] is item2

# Edge cases

def test_removing_first_item_when_it_is_current_item(folders):
    
    input_folder, output_folder = folders
    queue = Queue()
    item = queue.add_item(input_folder, output_folder)
    item2 = queue.add_item(input_folder, output_folder)

    queue.current_index = 0
    removed = queue.remove_item(0)

    assert queue.current_index is None
    assert queue.items[0] is item2
    assert removed is item
    assert len(queue.items) == 1

def test_remove_item_in_sequence_current_index_middle(queue_with_three_items):

    queue, item1, item2, item3 = queue_with_three_items

    queue.current_index = 1  
    removed1 = queue.remove_item(0)

    assert removed1 is item1
    assert queue.current_index == 0
    assert len(queue.items) == 2
    assert queue.items[0] is item2

    removed2 = queue.remove_item(1)

    assert removed2 is item3
    assert queue.current_index == 0
    assert len(queue.items) == 1
    assert queue.items[0] is item2