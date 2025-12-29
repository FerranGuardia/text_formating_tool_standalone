"""
PDF Builder Module

Orchestrates all PDF formatter components to build the final PDF document.
Coordinates the workflow from text files to finished PDF.
"""

from pathlib import Path
from typing import Optional

from src.pdf_formatter.text_merger import TextMerger
from src.pdf_formatter.text_cleaner import TextCleaner
from src.pdf_formatter.spacing_formatter import SpacingFormatter
from src.pdf_formatter.pagination_handler import PaginationHandler
from src.pdf_formatter.title_handler import TitleHandler
from src.pdf_formatter.index_generator import IndexGenerator
from src.pdf_formatter.metadata_handler import MetadataHandler


class PDFBuilder:
    """
    Orchestrates PDF building process.
    
    Coordinates all formatter components to transform text files
    into a formatted PDF document.
    """
    
    def __init__(self, input_folder: str, output_folder: str):
        """
        Initialize the PDFBuilder.
        
        Args:
            input_folder: Path to folder containing text files
            output_folder: Path to folder where PDF will be saved
        """
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        
        # Initialize components
        self.text_merger = TextMerger(input_folder)
        self.text_cleaner = TextCleaner()
        self.spacing_formatter = SpacingFormatter()
        self.pagination_handler = PaginationHandler()
        self.title_handler = TitleHandler()
        self.index_generator = IndexGenerator()
        self.metadata_handler = MetadataHandler()
    
    def build_pdf(self, title: Optional[str] = None, 
                  author: Optional[str] = None,
                  cover_image: Optional[Path] = None) -> Path:
        """
        Build the complete PDF document.
        
        Orchestrates the entire process:
        1. Merge text files
        2. Clean text
        3. Format spacing
        4. Handle titles
        5. Add pagination
        6. Generate index/TOC
        7. Add metadata/cover
        8. Create final PDF
        
        Args:
            title: Book title (optional)
            author: Author name (optional)
            cover_image: Path to cover image (optional)
            
        Returns:
            Path to the created PDF file
        """
        pass
    
    def _process_text(self) -> str:
        """
        Process text through all formatting stages.
        
        Returns:
            Fully processed text ready for PDF generation
        """
        pass
    
    def _generate_pdf(self, processed_text: str, metadata: dict) -> Path:
        """
        Generate the actual PDF file.
        
        Args:
            processed_text: Fully processed text content
            metadata: PDF metadata dictionary
            
        Returns:
            Path to created PDF file
        """
        pass

