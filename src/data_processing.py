import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(path):
    df = pd.read_csv(path)
    return df


def preprocess_data(df):

    df = df.drop("Loan_ID", axis=1)

    # Categorical
    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
    df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
    df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
    df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

    # Numerical
    df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
    df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())

    # Special case
    df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

    # Encoding
    label_cols = [
        "Gender", "Married", "Education",
        "Self_Employed", "Property_Area", "Dependents"
    ]

    le = LabelEncoder()

    for col in label_cols:
        df[col] = le.fit_transform(df[col])

    # Target
    df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

    return df


def split_data(df):

    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


def preprocess_input(input_dict):

    import pandas as pd

    df = pd.DataFrame([input_dict])

    # Same transformations as training
    # (must match exactly)

    # Encoding mappings (IMPORTANT: must be consistent)
    mappings = {
        "Gender": {"Male": 1, "Female": 0},
        "Married": {"Yes": 1, "No": 0},
        "Education": {"Graduate": 0, "Not Graduate": 1},
        "Self_Employed": {"Yes": 1, "No": 0},
        "Property_Area": {"Urban": 2, "Rural": 0, "Semiurban": 1},
        "Dependents": {"0": 0, "1": 1, "2": 2, "3+": 3}
    }

    for col, mapping in mappings.items():
        if col in df:
            df[col] = df[col].map(mapping)

    return df