# train.py

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

obj = DataIngestion()

train_path, test_path = obj.initiate_data_ingestion()

data_transformation = DataTransformation()

train_arr, test_arr, _ = (
    data_transformation
    .initiate_data_transformation(
        train_path,
        test_path
    )
)

trainer = ModelTrainer()

score = trainer.initiate_model_trainer(
    train_arr,
    test_arr
)

print("R2 Score:", score)