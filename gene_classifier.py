import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import argparse

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    X = df.drop('label', axis=1)
    y = df['label']

    le = LabelEncoder()
    y = le.fit_transform(y)  # FLT = 1, GC = 0

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, preds))
    print("\nClassification Report:")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gene Expression Classifier")
    parser.add_argument("input_csv", help="Path to gene expression CSV file")
    args = parser.parse_args()

    X_train, X_test, y_train, y_test = load_and_prepare_data(args.input_csv)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
