from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
from typing import Tuple
import numpy as np


def load_data() -> Tuple[np.ndarray, np.ndarray]:
    data = load_iris()
    return data.data, data.target


def train_model() -> RandomForestClassifier:
    X, y = load_data()
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, path="model.joblib"):
    joblib.dump(model, path)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
