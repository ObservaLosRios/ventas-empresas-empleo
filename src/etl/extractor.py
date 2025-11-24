from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path
from typing import Any
from src.utils.logger import setup_logger

logger = setup_logger("Extractor")

class Extractor(ABC):
    """
    Abstract Base Class for Data Extraction.
    """
    @abstractmethod
    def extract(self, source: Any) -> pd.DataFrame:
        pass

class CSVExtractor(Extractor):
    """
    Concrete implementation of Extractor for CSV files.
    """
    def __init__(self, skip_rows: int = 0):
        self.skip_rows = skip_rows

    def extract(self, file_path: Path) -> pd.DataFrame:
        """
        Extracts data from a CSV file.
        """
        logger.info(f"Extracting data from {file_path}...")
        try:
            # Read CSV, skipping the specified number of rows
            df = pd.read_csv(file_path, skiprows=self.skip_rows)
            logger.info(f"Successfully extracted {len(df)} rows from {file_path.name}.")
            return df
        except Exception as e:
            logger.error(f"Failed to extract data from {file_path}: {e}")
            raise
