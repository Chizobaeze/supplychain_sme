import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def train_model(df):

    model_df = df.copy()

    model_df = model_df.drop(columns=[
        "loan_id",
        "application_date",
        "disbursement_date",
        "business_id"
    ])

    y = model_df["default_180d"]

    X = model_df.drop(columns=[
        "default_90d",
        "default_180d"
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    lr_model = LogisticRegression(max_iter=1000)

    lr_model.fit(X_train, y_train)

    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    lr_pred = lr_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)

    lr_acc = accuracy_score(y_test, lr_pred)
    rf_acc = accuracy_score(y_test, rf_pred)

    best_model = rf_model if rf_acc >= lr_acc else lr_model

    joblib.dump(best_model, "credit_risk_model.pkl")

    report = classification_report(y_test, rf_pred)

    matrix = confusion_matrix(y_test, rf_pred)

    feature_importance = None

    if hasattr(rf_model, "feature_importances_"):

        feature_importance = {
            "features": X.columns,
            "importance": rf_model.feature_importances_
        }

    return {
        "lr_accuracy": lr_acc,
        "rf_accuracy": rf_acc,
        "report": report,
        "matrix": matrix,
        "feature_importance": feature_importance
    }


def predict_risk(features):

    model = joblib.load("credit_risk_model.pkl")

    prediction = model.predict([features])

    return prediction[0]