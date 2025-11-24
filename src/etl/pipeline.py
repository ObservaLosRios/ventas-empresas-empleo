from pathlib import Path
from src.etl.extractor import Extractor
from src.etl.transformer import Transformer
from src.etl.loader import Loader
from src.utils.logger import setup_logger

logger = setup_logger("Pipeline")

class ETLPipeline:
    """
    Orchestrates the ETL process.
    """
    def __init__(self, extractor: Extractor, transformer: Transformer, loader: Loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self, source: Path, destination: Path):
        """
        Runs the ETL pipeline: Extract -> Transform -> Load.
        """
        logger.info(f"Starting ETL pipeline for {source.name}...")
        
        # Extract
        df = self.extractor.extract(source)
        
        # Transform
        df_transformed = self.transformer.transform(df)
        
        # Load
        self.loader.load(df_transformed, destination)
        
        logger.info(f"ETL pipeline finished for {source.name}.")
