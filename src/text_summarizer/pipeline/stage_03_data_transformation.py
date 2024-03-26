from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.logging import logger
from text_summarizer.utils.common import read_yaml
from text_summarizer.constants import *
from text_summarizer.conponents.data_transformation import DataTransformation

class DataTransformationPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        
