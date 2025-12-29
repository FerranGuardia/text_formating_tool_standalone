"""
PDF Formatter Module

Modular components for formatting text files into PDF documents.
Each module handles a specific aspect of PDF formatting.
"""

from src.pdf_formatter.text_merger import TextMerger
from src.pdf_formatter.text_cleaner import TextCleaner
from src.pdf_formatter.spacing_formatter import SpacingFormatter
from src.pdf_formatter.pagination_handler import PaginationHandler
from src.pdf_formatter.title_handler import TitleHandler
from src.pdf_formatter.index_generator import IndexGenerator
from src.pdf_formatter.metadata_handler import MetadataHandler
from src.pdf_formatter.pdf_builder import PDFBuilder

__all__ = [
    "TextMerger",
    "TextCleaner",
    "SpacingFormatter",
    "PaginationHandler",
    "TitleHandler",
    "IndexGenerator",
    "MetadataHandler",
    "PDFBuilder",
]

