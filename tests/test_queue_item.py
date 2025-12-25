import os
import pytest #tool used for unit test
from src.queue_item import QueueItem # this is to call the class i created

def test_queue_item_missing_file(tmp_path):
#pytest needs to have functions starting with test so it can read them.
    output = tmp_path / "out"
    output.mkdir() #mkdir = make directory

    with pytest.raises(FileNotFoundError): #pytest raises
        QueueItem("does_not_exist.txt", str(output))

def test_queue_item_missing_output_folder(tmp_path): 
    #tmp_path is a empty isolated fixuture. A temporary folder created just for this test.

    file = tmp_path / "example.txt" # you declare your willingness to create a txt file to that path
    file.write_text("hello") # turns path into a file that has hello wrote on it

    with pytest.raises(NotADirectoryError):
        QueueItem(str(file), "missing_folder")

def test_queue_item_valid(tmp_path):
    #this is to create a temporary path
    
    file = tmp_path / "example.txt"
    file.write_text("hello")

    #create a temporary output folder

    output = tmp_path /"out"
    output.mkdir()

    item = QueueItem(str(file), str(output))

    #Asertions
    assert item.file_name == "example.txt"
    assert item.file_path == str(file)
    assert item.output_folder == str(output)
    assert item.status == "Pending"
    assert item.progress == 0

