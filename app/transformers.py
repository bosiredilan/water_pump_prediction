import pandas as pd
import numpy as np


def create_pump_age(df):

    df = df.copy()

    # convert date
    df["date_recorded"] = pd.to_datetime(df["date_recorded"])

    # extract recorded year
    df["recorded_year"] = df["date_recorded"].dt.year

    # replace invalid construction years
    df["construction_year"] = np.where(
        df["construction_year"] == 0,
        np.nan,
        df["construction_year"]
    )

    # create age
    df["pump_age"] = (
        df["recorded_year"] -
        df["construction_year"]
    )

    # remove negative values
    df["pump_age"] = df["pump_age"].clip(lower=0)

    # fill missing values
    df["pump_age"] = df["pump_age"].fillna(
        df["pump_age"].median()
    )

    # remove helper columns
    df.drop(
        columns=["date_recorded", "recorded_year"],
        inplace=True
    )

    return df