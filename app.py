from flask import Flask
from flask import request
from flask import render_template
import json

from src.pipeline.predict_pipeline import (
    PredictPipeline,
    CustomData
)


app = Flask(__name__)


# Load EDA report once when server starts
with open("notebook/summary.json") as f:
    eda_data = json.load(f)



@app.route("/")
def index():

    return render_template(
        "home.html",
        data=eda_data
    )

@app.route("/predict")
def predict():

    return render_template(
        "predict.html"
    )


@app.route("/predictdata", methods=["POST"])
def predict_datapoint():


    data = CustomData(

        gender=request.form.get("gender"),

        race_ethnicity=request.form.get(
            "race_ethnicity"
        ),

        parental_level_of_education=
        request.form.get(
            "parental_level_of_education"
        ),

        lunch=request.form.get("lunch"),

        test_preparation_course=
        request.form.get(
            "test_preparation_course"
        ),

        reading_score=float(
            request.form.get(
                "reading_score"
            )
        ),

        writing_score=float(
            request.form.get(
                "writing_score"
            )
        )
    )


    pred_df = (
        data.get_data_as_dataframe()
    )


    pipeline = PredictPipeline()


    result = pipeline.predict(
        pred_df
    )


    return render_template(
        "predict.html",
        data=eda_data,
        results=round(
            float(result[0]),
            2
        )
    )



if __name__=="__main__":

    app.run(
        debug=True
    )