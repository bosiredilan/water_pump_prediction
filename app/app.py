from flask import Flask, render_template, request
import pandas as pd

from predictor import make_prediction

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = {
            "amount_tsh": float(request.form["amount_tsh"]),
            "gps_height": float(request.form["gps_height"]),
            "longitude": float(request.form["longitude"]),
            "latitude": float(request.form["latitude"]),
            "population": int(request.form["population"]),
            "construction_year": int(request.form["construction_year"]),

            "date_recorded": request.form["date_recorded"],

            "basin": request.form["basin"],
            "region": request.form["region"],
            "lga": request.form["lga"],
            "extraction_type": request.form["extraction_type"],
            "management": request.form["management"],
            "payment_type": request.form["payment_type"],
            "water_quality": request.form["water_quality"],
            "quantity": request.form["quantity"],
            "source_type": request.form["source_type"],
            "waterpoint_type": request.form["waterpoint_type"],
            "public_meeting": request.form["public_meeting"],
            "permit": request.form["permit"]
        }

        df = pd.DataFrame([data])

        #print("\n==============================")
        #print("INPUT DATAFRAME")
        #print(df)
        #print(df.dtypes)
        #print("==============================")

        prediction = make_prediction(df)

        #print("Prediction:", prediction)

        label_map = {
            0: "Functional",
            1: "Functional Needs Repair",
            2: "Non Functional"
        }

        result = label_map.get(prediction, prediction)

        return render_template(
            "index.html",
            prediction_text=f"Prediction: {result}"
        )

    except Exception as e:

        #print("\nERROR")
        #print(e)

        return render_template(
            "index.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)