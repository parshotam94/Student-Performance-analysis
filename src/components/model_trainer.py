import os
import sys
from dataclasses import dataclass

import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj


@dataclass
class ModelTrainerConfig:

    trained_model_file_path = os.path.join(
        "artifacts",
        "model.pkl"
    )


class ModelTrainer:

    def __init__(self):

        self.model_trainer_config = (
            ModelTrainerConfig()
        )

    def initiate_model_trainer(
        self,
        train_array,
        test_array
    ):

        try:

            logging.info(
                "Splitting Training and Testing Arrays"
            )

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            models = {
                "Linear Regression":
                LinearRegression(),

                "Decision Tree":
                DecisionTreeRegressor(),

                "Random Forest":
                RandomForestRegressor()
            }

            model_report = {}

            for model_name, model in models.items():

                model.fit(
                    X_train,
                    y_train
                )

                y_pred = model.predict(
                    X_test
                )

                score = r2_score(
                    y_test,
                    y_pred
                )

                model_report[model_name] = score

                logging.info(
                    f"{model_name} R2 Score : {score}"
                )

            best_model_score = max(
                sorted(model_report.values())
            )

            best_model_name = list(
                model_report.keys()
            )[
                list(
                    model_report.values()
                ).index(best_model_score)
            ]

            best_model = models[
                best_model_name
            ]

            logging.info(
                f"Best Model : {best_model_name}"
            )

            save_obj(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(
                X_test
            )

            r2_square = r2_score(
                y_test,
                predicted
            )

            logging.info(
                f"Final R2 Score : {r2_square}"
            )

            return r2_square

        except Exception as e:
            raise CustomException(e)