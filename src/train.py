import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from src.data_processing import load_data, preprocess_data, split_data


def train_model(data_path):

    # Load and preprocess
    df = load_data(data_path)
    df = preprocess_data(df)

    X_train, X_test, y_train, y_test = split_data(df)

    # Train model
    model = LogisticRegression(max_iter=100)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "model/model.pkl")

    print("\nModel saved at model/model.pkl")

    return model


if __name__ == "__main__":
    train_model("data/loan_data.csv")