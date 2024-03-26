from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.logging import logger
from text_summarizer.utils.common import read_yaml
from text_summarizer.constants import *
from text_summarizer.conponents.data_validation import DataValidation



class DataValidationPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()

    