from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from src.utils.logger import setup_logger

logger = setup_logger("Transformer")

class Transformer(ABC):
    """
    Abstract Base Class for Data Transformation.
    """
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class CleaningTransformer(Transformer):
    """
    Concrete implementation of Transformer for basic data cleaning.
    """
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies cleaning transformations to the DataFrame.
        """
        logger.info("Starting data transformation...")
        
        # 1. Clean Column Names
        df = self._clean_column_names(df)
        
        # 2. Drop empty columns (like 'Unnamed: ...' if they are empty)
        # We check if a column name starts with "unnamed" and drop it if it's mostly empty or just garbage
        # In the user's file, the first few columns were empty in the raw read, but since we skip rows, 
        # the header should be correct. However, sometimes trailing commas create empty columns.
        df = df.loc[:, ~df.columns.str.contains('^unnamed', case=False)]

        # 3. Drop rows that are completely empty
        original_count = len(df)
        df.dropna(how='all', inplace=True)
        dropped_count = original_count - len(df)
        if dropped_count > 0:
            logger.info(f"Dropped {dropped_count} completely empty rows.")

        logger.info("Data transformation completed.")
        return df

    def _clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardizes column names to snake_case.
        """
        df.columns = (df.columns
                      .str.strip()
                      .str.lower()
                      .str.replace(' ', '_')
                      .str.replace('(', '')
                      .str.replace(')', '')
                      .str.replace('/', '_')
                      .str.replace('.', '')
                      .str.replace(',', '')
                      )
        return df
