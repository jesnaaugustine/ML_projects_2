import os
import sys
from  src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import dataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path= os.path.join('artifacts','train.csv')
    test_data_path= os.path.join('artifacts','test.csv')
    raw_data_path= os.path.join('artifacts','data.csv')
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered data ingestion method')
        try:
            df= pd.read_csv('notebooks/data/StudentsPerformance.csv')
            logging.info('read dataset')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #to create nested directories use this instead of mkdir
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train test split started')
            train_data,test_data= train_test_split(df,test_size=0.2,random_state=40)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('ingestion completed')
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
   obj=DataIngestion()
   train_data,test_data=obj.initiate_data_ingestion()

   data_transformation=dataTransformation()
   train_arr,test_arr,_=data_transformation.initate_data_trans(train_data,test_data)

    


