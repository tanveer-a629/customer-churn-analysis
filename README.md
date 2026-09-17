# 📊 Customer Churn Analysis & Prediction

An end-to-end customer churn analytics and prediction project built using SQL, Python, Machine Learning, and Power BI.

The project combines data preparation, data quality validation, business analysis, customer churn prediction, and interactive dashboards to identify churn patterns, understand customer risk, and support data-driven retention decisions.

---

## 📌 Project Overview

Customer churn is an important business problem because losing existing customers can directly impact revenue and long-term growth.

This project analyzes customer data to understand:

- Customer churn patterns
- Customer demographics and account information
- Contract and payment behavior
- Service usage
- Churn categories and reasons
- Geographic churn patterns
- High-risk customer segments
- Revenue exposure from predicted churners

A Random Forest classification model was developed in Python to predict potential churners.

The predictions were integrated into Power BI to create interactive Churn Prediction and Retention & Risk analysis.

---

## 🎯 Business Objectives

The main objectives of this project are to:

- Analyze historical customer churn patterns
- Identify customer segments with higher churn rates
- Understand major churn categories and reasons
- Analyze churn across contracts, payment methods, services, and states
- Perform data quality validation before analysis
- Build a machine learning model for churn prediction
- Identify customers with predicted churn risk
- Estimate revenue exposure from predicted churners
- Provide retention-focused business insights through Power BI

---

## ❓ Business Questions

This project addresses questions such as:

- What is the overall customer churn rate?
- Which contract types have higher churn?
- Which payment methods are associated with higher churn?
- Which customer segments show higher churn rates?
- Which states have higher customer churn?
- Which internet and additional services are associated with churn?
- What are the major reasons behind customer churn?
- How many customers are predicted to churn?
- Which customer groups represent higher potential risk?
- How much monthly revenue is exposed to predicted churn?
- Which retention actions can be considered for different customer risk segments?

---

## 📂 Dataset

The project uses customer-level data containing information related to:

- Customer demographics
- Account information
- Contract details
- Payment methods
- Internet and service usage
- Tenure
- Monthly charges
- Total revenue
- Churn status
- Churn category
- Churn reason

The data was prepared and validated before being used for analysis and machine learning.

---

## 🔄 Data Preparation & Validation

Data preparation was performed using SQL Server / SSMS and Power Query.

### Data Preparation Process

1. Loaded customer data into SQL Server.
2. Performed data quality and NULL-value checks.
3. Validated customer records and important fields.
4. Cleaned and transformed the dataset.
5. Created analytical database objects and reporting views.
6. Performed additional transformations using Power Query.
7. Created calculated fields and measures required for Power BI.
8. Prepared prediction data for the machine learning workflow.

### Data Quality Focus

The project specifically considers:

- NULL values
- Duplicate records
- Data type consistency
- Customer status validation
- Age group classification
- Tenure group classification
- Service-related data preparation

---

## 🧮 SQL Analysis

SQL was used for data preparation, validation, transformation, and business analysis.

The SQL workflow includes:

- Customer distribution analysis
- Contract analysis
- Customer status analysis
- Revenue analysis
- State-wise customer distribution
- Churn analysis
- NULL-value validation
- Data quality checks
- Production table preparation
- Reporting views
- Aggregation and grouping
- Business-oriented analytical queries

SQL was used as an important layer between the raw customer data and the Power BI reporting layer.

---

## 🤖 Machine Learning – Churn Prediction

A Random Forest Classifier was developed using Python to predict potential customer churn.

### Target Variable

Customer_Status

Stayed  → 0
Churned → 1

### Model Workflow

The machine learning process includes:

- Data preprocessing
- Removing non-predictive customer identifiers
- Removing churn category and churn reason fields from model inputs
- Encoding categorical variables
- Splitting data into training and testing datasets
- Training a Random Forest classification model
- Evaluating the model
- Generating churn predictions
- Identifying predicted churn customers
- Exporting prediction results for Power BI analysis

The prediction workflow is designed to identify customers who may be at higher risk of churn based on their available customer and service attributes.

---

## 📊 Power BI Dashboard

The Power BI report contains four main analytical pages:

### 1. Churn Analysis – Summary

Provides an overall view of customer churn and major customer characteristics.

Key metrics include:

- Total Customers: 6,418
- New Joiners: 411
- Total Churn: 1,732
- Churn Rate: 27.0%

The dashboard analyzes:

- Churn by Gender
- Customers and Churn Rate by Age Group
- Churn Rate by State
- Churn Rate by Internet Type
- Churn Rate by Payment Method
- Churn Rate by Contract
- Customers and Churn Rate by Tenure Group
- Churn Distribution by Category
- Churn by Services

### 2. Churn Analysis – Churn Reason

This page focuses on understanding the reasons behind customer churn.

It provides a detailed view of churn reasons such as:

- Attitude of service provider
- Attitude of support person
- Competitor-related reasons
- Pricing-related reasons
- Service and support issues
- Data/service-related issues
- Other recorded churn reasons

This helps connect the overall churn count with the underlying reasons reported by customers.

### 3. Churn Analysis – Prediction

This page focuses on the output of the machine learning prediction workflow.

It provides:

- Predicted churner count
- Predicted churner profile
- Gender distribution
- Age group distribution
- Marital status distribution
- Tenure group distribution
- Payment method distribution
- Contract distribution
- State-wise predicted churner distribution
- Customer-level predicted churner table

The customer-level table allows predicted churners to be reviewed using fields such as:

- Customer ID
- Monthly Charge
- Total Revenue
- Total Refunds
- Number of Referrals
- Other available customer attributes

### 4. Churn Analysis – Retention & Risk

This page converts churn predictions into a business-focused risk and retention view.

Key metrics include:

- Total Revenue Lost: 3M
- Revenue at Risk: 138.37K
- Target Saved Revenue: 27.67K
- Avg Tenure – Risk Customers: 17.37

The page includes:

- Customer Risk Tier
- Key Churn Driver
- Financial Impact
- Recommended Action
- Revenue at Risk by Contract and Churn Category
- Revenue at Risk by Payment Method
- Revenue at Risk by State
- Revenue at Risk by Contract
- Revenue at Risk vs Target Goal
- Revenue at Risk Share by Churn Category
- Customer-level revenue-at-risk table

This page connects machine learning predictions with business-oriented retention analysis.

---

## 📈 Key Metrics

| Metric | Value |
|---|---:|
| Total Customers | 6,418 |
| New Joiners | 411 |
| Total Churn | 1,732 |
| Churn Rate | 27.0% |
| Predicted Churners | 2,054 |
| Revenue at Risk | 138.37K |
| Target Saved Revenue | 27.67K |
| Avg Tenure – Risk Customers | 17.37 |
| Total Revenue Lost | 3M |

---

## 💡 Key Insights

The analysis identifies several important patterns in the customer dataset:

- Month-to-month customers show a substantially higher churn rate than longer-term contract customers.
- Churn varies across different payment methods.
- Internet service type shows differences in customer churn rates.
- Churn patterns vary across geographic regions.
- Customer tenure is an important dimension for understanding churn behavior.
- Competitor-related, attitude-related, pricing-related, and service-related reasons contribute to customer churn.
- The prediction dashboard identifies 2,054 customers as potential churners.
- Predicted churners can be further analyzed by demographics, tenure, contract, payment method, and state.
- The Retention & Risk dashboard connects predicted churners with monthly charges to estimate 138.37K in revenue at risk.
- Risk-based analysis helps translate customer-level predictions into business-focused retention opportunities.

---

## 🎯 Retention & Risk Approach

The project extends beyond simply counting historical churn.

The Retention & Risk dashboard uses predicted churn customers to create a business-oriented view of potential financial exposure.

The analysis considers:

Predicted Churners
        ↓
Customer Risk Segmentation
        ↓
Key Churn Drivers
        ↓
Financial Impact
        ↓
Revenue at Risk
        ↓
Recommended Retention Action

This approach helps move the analysis from "Who churned?" toward "Who may churn, what is the potential impact, and where should retention efforts be focused?"

---

## 📊 Dashboard Preview

### 1. Churn Analysis – Summary

![Churn Analysis Summary](Screenshots/Churn%20Summary.png)

### 2. Churn Analysis – Churn Prediction

![Churn Analysis Churn Prediction](Screenshots/Churn%20Prediction.png)

### 3. Churn Analysis – Retention & Risk

![Churn Analysis Retention & Risk](Screenshots/Retention%20%26%20Risk.png)

### 4. Churn Analysis – Churn Reason

![Churn Analysis Churn Reason](Screenshots/Churn%20Reason.png)

---

## 🔄 Project Workflow

Raw Customer Data  
↓  
SQL Server / SSMS  
↓  
Data Cleaning & Validation  
↓  
SQL Analysis & Reporting Views  
↓  
Power Query Transformations  
↓  
Prepared Analytical Dataset  
↓  
Python Preprocessing  
↓  
Random Forest Model  
↓  
Churn Prediction  
↓  
Predicted Churn Customers  
↓  
Power BI  
↓  
Summary + Churn Prediction + Retention & Risk + Churn Reason  
↓  
Business Insights

---

## 🛠️ Tools & Technologies

- SQL Server
- SQL Server Management Studio (SSMS)
- SQL
- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Power Query
- Power BI
- DAX
- Excel / CSV
- GitHub

---

## 📁 Repository Structure

Customer-Churn-Analysis/
├── Codes/
│   ├── DAX_Measures_Combined.txt
│   ├── Power_Query_Transformations.txt
│   ├── SQL_Queries.sql
│   ├── churn_prediction_model.py
│   ├── predict_churn.py
│   └── README.md
│
├── Data/
│   ├── Customer_Data.xlsx
│   └── Prediction Data.xlsx
│
├── Output/
│   └── Predicted_Churn_Customers.csv
│
├── Screenshots/
│   ├── Churn Summary.png
│   ├── Churn Prediction.png
│   ├── Retention & Risk.png
│   └── Churn Reason.png
│
├── Churn Analysis.pbix
└── README.md
---

## ▶️ How to Run

### SQL Analysis

1. Install Microsoft SQL Server and SSMS.
2. Create the required database.
3. Import the customer dataset.
4. Open the SQL script from the Codes folder.
5. Execute the SQL queries and data preparation steps.
6. Verify the analytical tables and views.

### Python Machine Learning

1. Install Python and the required libraries.
2. Place the prediction dataset in the required location.
3. Run the model training script.
4. The Random Forest model is trained using the prepared customer data.
5. Run the prediction script.
6. Generate the predicted churn customer output.
7. Use the prediction output for Power BI analysis.

### Power BI

1. Open Churn Analysis.pbix.
2. Check the data source connections.
3. Refresh the dataset if required.
4. Explore the four dashboard pages:
   - Summary
   - Churn Reason
   - Churn Prediction
   - Retention & Risk

---

## 📌 Project Highlights

- End-to-end customer churn analytics workflow
- SQL-based data preparation and validation
- Business-oriented churn analysis
- Machine learning-based churn prediction
- Customer-level predicted churn output
- Power BI interactive reporting
- DAX-based KPI and revenue calculations
- Revenue-at-risk analysis
- Retention-focused business insights

---

## 🎯 Project Objective

The main objective of this project is to demonstrate practical skills in:

- SQL data analysis
- Data cleaning and validation
- Data transformation
- ETL concepts
- Python data processing
- Machine learning
- Classification modeling
- Churn prediction
- Power BI dashboard development
- DAX calculations
- Business analytics
- Data-driven decision making

---

## ✅ Conclusion

This project demonstrates a complete customer churn analytics workflow, starting from data preparation and SQL analysis and extending to machine learning-based churn prediction and business-focused Power BI reporting.

By combining SQL, Python, Machine Learning, Power BI, and DAX, the project provides both historical churn analysis and forward-looking customer risk analysis.

The four dashboard pages — Summary, Churn Reason, Churn Prediction, and Retention & Risk — provide different levels of analysis, from understanding overall churn patterns to identifying potential churners and estimating revenue exposure.

---

## ⭐ Project Highlight

> From historical churn analysis to predictive customer risk — this project combines SQL, Python Machine Learning, and Power BI to identify potential churners, understand churn drivers, and quantify revenue at risk for retention-focused decision making.

---

## 👤 Author

**Tanveer Ahmad**

B.Tech – Computer Science & Engineering (Data Science)

GitHub: [tanveer-a629](https://github.com/tanveer-a629)
