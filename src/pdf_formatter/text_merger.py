"""
Text Merger Module

Responsible for reading and merging multiple text files from a directory
into a single continuous text string, maintaining proper chapter order.
"""

from pathlib import Path
from typing import List


class TextMerger:
    """
    Merges multiple text files into a single text string.
    
    Reads all .txt files from an input folder, sorts them by chapter number,
    and merges them into one continuous text string.
    """
    
    def __init__(self, input_folder: str):
        """
        Initialize the TextMerger.
        
        Args:
            input_folder: Path to folder containing text files to merge
        """
        self.input_folder = Path(input_folder)
        self.text_files: List[Path] = []
    
    def find_text_files(self) -> List[Path]:
        """
        Find all .txt files in the input folder.
        
        Returns:
            List of Path objects for all .txt files found
        """
        pass
    
    def sort_files_by_chapter(self, files: List[Path]) -> List[Path]:
        """
        Sort text files by chapter number.
        
        Extracts chapter number from filename (e.g., chapter_0001_...)
        and sorts files in ascending order.
        
        Args:
            files: List of file paths to sort
            
        Returns:
            Sorted list of file paths
        """
        pass
    
    def merge_files(self) -> str:
        """
        Merge all text files into a single string.
        
        Reads each file in order and concatenates their contents
        with appropriate separators.
        
        Returns:
            Merged text content as a single string
        """
        pass

