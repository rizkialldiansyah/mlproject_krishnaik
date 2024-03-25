from fastapi import FastAPI
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import uvicorn
from src.logger import logger
from pydantic import BaseModel

class User_input(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int

app = FastAPI()
logger.info('Starting API...')

@app.get("/")
def read_root():
    return {"Intro": "Here is the API Model for Study Score Prediction."}


@app.post("/predict")
def predict_custome_data(input: User_input):
    data=CustomData(
        gender=input.gender,
        race_ethnicity=input.race_ethnicity,
        parental_level_of_education=input.parental_level_of_education,
        lunch=input.lunch,
        test_preparation_course=input.test_preparation_course,
        reading_score=input.reading_score,
        writing_score=input.writing_score
    )
    data_df=data.get_data_as_dataframe()
    predict_pipline=PredictPipeline()
    logger.info('Predict input data...')
    result=predict_pipline.predict(data_df)
    return {"math_score_predicted": result[0]}

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)