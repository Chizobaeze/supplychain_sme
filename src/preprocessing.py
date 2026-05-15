from sklearn.preprocessing import LabelEncoder


def preprocess(df):

    df = df.copy()

    categorical_cols = [
        "business_sector",
        "business_state",
        "lender"
    ]

    encoder = LabelEncoder()

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df