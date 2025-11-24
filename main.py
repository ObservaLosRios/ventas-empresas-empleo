import os
from pathlib import Path
from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, SKIP_ROWS
from src.etl.extractor import CSVExtractor
from src.etl.transformer import CleaningTransformer
from src.etl.loader import CSVLoader
from src.etl.pipeline import ETLPipeline
from src.utils.logger import setup_logger

logger = setup_logger("Main")

def main():
    logger.info("Initializing ETL Process...")

    # Initialize components
    extractor = CSVExtractor(skip_rows=SKIP_ROWS)
    transformer = CleaningTransformer()
    loader = CSVLoader()
    
    # Initialize Pipeline
    pipeline = ETLPipeline(extractor, transformer, loader)

    # Process all CSV files in the raw data directory
    if not RAW_DATA_DIR.exists():
        logger.error(f"Raw data directory {RAW_DATA_DIR} does not exist.")
        return

    files = list(RAW_DATA_DIR.glob("*.csv"))
    if not files:
        logger.warning(f"No CSV files found in {RAW_DATA_DIR}.")
        return

    for file_path in files:
        output_filename = f"clean_{file_path.name}"
        destination_path = PROCESSED_DATA_DIR / output_filename
        
        try:
            pipeline.run(file_path, destination_path)
        except Exception as e:
            logger.error(f"ETL failed for {file_path.name}. Skipping...")

    logger.info("All ETL jobs completed.")

if __name__ == "__main__":
    main()
