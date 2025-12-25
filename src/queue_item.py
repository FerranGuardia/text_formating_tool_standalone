class QueueItem:
    def _inint__(self, file_path, output_folder):
        self.file_path = file_path  #this is the location of the file
        self.output_folder = output_folder #this is where the file will be placed
        self.status = "Pending" #this is the default status when you add an item to the queue
        self.progress = 0 #this is to show the progress until completion