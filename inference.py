import joblib
import numpy as np

from models import IrisClass


def load_model(path="model.joblib"):
    try:
        return joblib.load(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file not found at path: {path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the model: {e}")


def predict(model, features: dict) -> str:
    try:
        data = np.array(
            [
                [
                    features["sepal_length"],
                    features["sepal_width"],
                    features["petal_length"],
                    features["petal_width"],
                ]
            ]
        )
        prediction = model.predict(data)
        return IrisClass(str(prediction[0])).name
    except KeyError as e:
        raise KeyError(f"Missing feature in input: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during prediction: {e}")
