import os

class QueueItem:

    def __init__(self, input_folder: str, output_folder: str):
        # --- Validation ---
        if not os.path.isdir(input_folder):
            raise NotADirectoryError(f"Input folder does not exist: {input_folder}")

        if not os.path.isdir(output_folder):
            raise NotADirectoryError(f"Output folder does not exist: {output_folder}")

        # --- Initialization ---
        self.input_folder: str = input_folder
        self.output_folder: str = output_folder
        self.status: str = "Pending"
        self.progress: int = 0

    # --- Methods ---
    def start(self):
        if self.status not in ("Pending", "Paused"):
            raise RuntimeError("Cannot start an item that is not pending.")
        self.status = "Processing"

    def pause(self):
        if self.status != "Processing":
            raise RuntimeError("Cannot pause an item that is not processing")
        self.status = "Paused"

    def resume(self):
        if self.status != "Paused":
            raise RuntimeError("Cannot resume this item")
        self.status = "Processing"

    def complete(self):
        if self.status != "Processing":
            raise RuntimeError("Cannot complete this item")
        self.status = "Completed"
