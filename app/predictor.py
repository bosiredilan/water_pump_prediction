from pathlib import Path
import joblib

# project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "water_pump_pipeline.joblib"

pipeline = joblib.load(MODEL_PATH)


def make_prediction(df):

    prediction = pipeline.predict(df)

    return prediction[0]