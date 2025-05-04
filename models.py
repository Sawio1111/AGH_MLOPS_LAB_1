from pydantic import BaseModel
from enum import Enum


class IrisClass(str, Enum):
    SETOSA = "0"
    VERSICOLOR = "1"
    VIRGINICA = "2"


class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class PredictResponse(BaseModel):
    prediction: str
