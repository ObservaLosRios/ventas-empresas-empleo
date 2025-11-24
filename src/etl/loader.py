from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger("Loader")

class Loader(ABC):
    """
    Abstract Base Class for Data Loading.
    """
    @abstractmethod
    def load(self, df: pd.DataFrame, destination: Path):
        pass

class CSVLoader(Loader):
    """
    Concrete implementation of Loader for CSV files.
    """
    def load(self, df: pd.DataFrame, destination: Path):
        """
        Saves the DataFrame to a CSV file.
        """
        logger.info(f"Loading data to {destination}...")
        try:
            df.to_csv(destination, index=False)
            logger.info(f"Successfully saved data to {destination}.")
        except Exception as e:
            logger.error(f"Failed to save data to {destination}: {e}")
            raise
