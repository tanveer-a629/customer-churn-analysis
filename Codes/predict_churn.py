"""
Customer Churn Analysis & Prediction
Prediction on New Customers

Purpose:
Load the trained Random Forest model and categorical encoders,
predict churn for new/joined customers, and export the customers
predicted as churned.
"""

import pandas as pd
import joblib


# ============================================================
# 1. LOAD TRAINED MODEL AND ENCODERS
# ============================================================

rf_model = joblib.load(
    "random_forest_churn_model.pkl"
)

label_encoders = joblib.load(
    "label_encoders.pkl"
)


# ============================================================
# 2. LOAD NEW CUSTOMER DATA
# ============================================================

file_path = r"C:\yourpath\Prediction_Data.xlsx"
sheet_name = "Vw_JoincData"

new_data = pd.read_excel(
    file_path,
    sheet_name=sheet_name
)

print("First five rows:")
print(new_data.head())


# Keep the original data so Customer_ID and original
# categorical values remain available in the output.
original_data = new_data.copy()


# ============================================================
# 3. PREPARE DATA FOR PREDICTION
# ============================================================

new_data = new_data.drop(
    [
        "Customer_ID",
        "Customer_Status",
        "Churn_Category",
        "Churn_Reason"
    ],
    axis=1
)

# Apply the same encoders fitted during model training.
for column in new_data.select_dtypes(include=["object"]).columns:
    new_data[column] = label_encoders[column].transform(
        new_data[column]
    )


# ============================================================
# 4. PREDICT CHURN
# ============================================================

new_predictions = rf_model.predict(new_data)

original_data["Customer_Status_Predicted"] = new_predictions


# ============================================================
# 5. FILTER PREDICTED CHURNERS
# ============================================================

predicted_churners = original_data[
    original_data["Customer_Status_Predicted"] == 1
].copy()

print(
    f"\nPredicted churners: {len(predicted_churners)}"
)


# ============================================================
# 6. EXPORT RESULTS
# ============================================================

output_path = r"C:\yourpath\Predictions.csv"

predicted_churners.to_csv(
    output_path,
    index=False
)

print(f"Predictions saved to: {output_path}")
