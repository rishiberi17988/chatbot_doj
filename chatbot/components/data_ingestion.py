from chatbot.logger.logger import logging
from chatbot.exception.exception import DojException
from langchain_community.document_loaders import UnstructuredURLLoader

import os 
import sys 


from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
KAGGLE_USERNAME=os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY=os.getenv("KAGGLE_KEY")
groq_api_key=os.getenv("groq_api_key")


class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e :
            raise DojException(e,sys)
        

    def parse_all_the_data():
        try:
            pass
        except Exception as e :
            raise DojException(e,sys)
        
    
    def parse_all_the_data():
        try:
            pass
        except Exception as e :
            raise DojException(e,sys)
        

    def parse_all_the_data():
        try:
            pass
        except Exception as e :
            raise DojException(e,sys)
        

    def parse_all_the_data():
        try:
            pass
        except Exception as e :
            raise DojException(e,sys)
