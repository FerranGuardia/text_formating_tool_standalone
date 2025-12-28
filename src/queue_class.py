from src.queue_item import QueueItem

#---Manager---
class Queue:
    
 def __init__(self):
    self.items = []
    self.current_index = None
    
 @property
 def current_item(self):
    if self.current_index is None:
        return None
    return self.items[self.current_index]
  
  #---Methods---

  def add_item(self, input_folder: str, output_folder: str):
    item = QueueItem(input_folder, output_folder)
    self.items.append(item)
    return item
