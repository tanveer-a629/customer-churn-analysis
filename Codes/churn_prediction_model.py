"""
Customer Churn Analysis & Prediction
Random Forest Model Training

Purpose:
Train a Random Forest classifier on historical churn data,
evaluate the model, inspect feature importance, and save the
trained model and categorical encoders for later prediction.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder


# ============================================================
# 1. LOAD DATA
# ============================================================

file_path = r"C:\yourpath\Prediction_Data.xlsx"
sheet_name = "Vw_ChurncData"

data = pd.read_excel(file_path, sheet_name=sheet_name)

print("First five rows:")
print(data.head())


# ============================================================
# 2. DATA PREPROCESSING
# ============================================================

# Remove columns that are not used as model features.
data = data.drop(
    ["Customer_ID", "Churn_Category", "Churn_Reason"],
    axis=1
)

# Categorical columns to encode.
columns_to_encode = [
    "Gender",
    "Married",
    "State",
    "Value_Deal",
    "Phone_Service",
    "Multiple_Lines",
    "Internet_Service",
    "Internet_Type",
    "Online_Security",
    "Online_Backup",
    "Device_Protection_Plan",
    "Premium_Support",
    "Streaming_TV",
    "Streaming_Movies",
    "Streaming_Music",
    "Unlimited_Data",
    "Contract",
    "Paperless_Billing",
    "Payment_Method"
]

# Fit and store one encoder for each categorical column.
label_encoders = {}

for column in columns_to_encode:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])


# Encode the target variable.
data["Customer_Status"] = data["Customer_Status"].map(
    {
        "Stayed": 0,
        "Churned": 1
    }
)

# Features and target.
X = data.drop("Customer_Status", axis=1)
y = data["Customer_Status"]


# ============================================================
# 3. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 4. TRAIN RANDOM FOREST
# ============================================================

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)


# ============================================================
# 5. MODEL EVALUATION
# ============================================================

y_pred = rf_model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# 6. FEATURE IMPORTANCE
# ============================================================

importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(15, 6))

sns.barplot(
    x=importances[indices],
    y=X.columns[indices]
)

plt.title("Random Forest Feature Importances")
plt.xlabel("Relative Importance")
plt.ylabel("Feature Names")
plt.tight_layout()
plt.show()


# ============================================================
# 7. SAVE MODEL AND ENCODERS
# ============================================================

joblib.dump(
    rf_model,
    "random_forest_churn_model.pkl"
)

joblib.dump(
    label_encoders,
    "label_encoders.pkl"
)

print("\nModel saved as: random_forest_churn_model.pkl")
print("Encoders saved as: label_encoders.pkl")
