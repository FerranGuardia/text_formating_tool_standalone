import os #this is a python module that will allow me to interact with the os.

class QueueItem:

    def _init__(self, file_path, output_folder):

        #---Validation ---

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Input file does not exist: {file_path}") #this checks if the input file exist. If it doesn't raises an error
        
        if not os.path.isdir(output_folder):
            raise NotADirectoryError(f"Output folder does not exist: {output_folder}") #this checks if the output folder exist. If it doesn't raises an error


        self.file_path = file_path  #this is the location of the file
        self.file_name = os.path.basename(file_path) #this line extracts a full path and figures out the file name
        self.output_folder = output_folder #this is where the file will be placed
        self.status = "Pending" #this is the default status when you add an item to the queue
        self.progress = 0 #this is to show the progress until completion
        