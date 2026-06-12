# Data ingestion placeholder. Read CSV, split train/test, save artifacts.
import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging


# Path of original dataset
DATASET_PATH = "notebook/dataset/StudentsPerformance.csv"


@dataclass
class DataIngestionConfig:
    """
    Stores all output file paths generated
    during data ingestion.
    """

    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    """
    Reads dataset and creates:
    1. raw.csv
    2. train.csv
    3. test.csv
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Data Ingestion Started")

        try:
            # Read Dataset
            df = pd.read_csv(DATASET_PATH)

            logging.info("Dataset loaded successfully")

            # Create artifacts folder
            os.makedirs("artifacts", exist_ok=True)

            # Save Raw Dataset
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info("Raw dataset saved")

            # Train Test Split
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            ) 

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info("Train Test Split Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) #save train.csv, test.csv

        except Exception as e:
            raise CustomException(e)