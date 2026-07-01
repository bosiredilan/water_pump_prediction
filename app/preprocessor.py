from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


numerical_features = [
    'amount_tsh',
    'gps_height',
    'longitude',
    'latitude',
    'population',
    'construction_year',
    'pump_age'
]

categorical_features = [
    'basin',
    'region',
    'lga',
    'extraction_type',
    'management',
    'payment_type',
    'water_quality',
    'quantity',
    'source_type',
    'waterpoint_type',
    'public_meeting',
    'permit'
]


def create_preprocessor():

    preprocessor = ColumnTransformer(
        transformers=[
            (
                'num',
                StandardScaler(),
                numerical_features
            ),
            (
                'cat',
                OneHotEncoder(
                    handle_unknown='ignore'
                ),
                categorical_features
            )
        ]
    )

    return preprocessor