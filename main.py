from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.text_summarizer.logging import logger
STAGE_NAME = "Data Ingetion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e) 
    raise e