import joblib

pipeline = joblib.load("models/water_pump_pipeline.joblib")

# print("Pipeline Loaded Successfully")


def make_prediction(df):

    #print("\n========== BEFORE PIPELINE ==========")
    #print(df)
    #print(df.columns.tolist())

    prediction = pipeline.predict(df)

    #print("\n========== AFTER PIPELINE ==========")
    #print(prediction)

    return prediction[0]