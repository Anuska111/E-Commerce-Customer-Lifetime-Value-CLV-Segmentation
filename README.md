
# 📊 E-Commerce Customer Lifetime Value (CLV) Prediction & Customer Segmentation

> An end-to-end Machine Learning project that predicts Customer Lifetime Value (CLV) and segments customers using RFM Analysis, K-Means Clustering, and Random Forest Regression to help businesses improve customer retention and maximize revenue.

---
![Heatmap]Images<img width="1080" height="776" alt="image" src="https://github.com/user-attachments/assets/b425af88-39c6-4384-a4f8-690f0441bf07" />

# 🚀 Project Overview

Customer Lifetime Value (CLV) is one of the most important business metrics in e-commerce. It estimates the total value a customer is expected to generate throughout their relationship with a business.

This project develops a complete Machine Learning pipeline that:

- Cleans and preprocesses e-commerce transaction data.
- Performs Exploratory Data Analysis (EDA).
- Creates RFM (Recency, Frequency, Monetary) features.
- Segments customers using K-Means Clustering.
- Predicts Customer Lifetime Value (CLV) using Random Forest Regression.
- Evaluates model performance using multiple metrics.
- Generates business insights for customer retention strategies.

---

# 🎯 Objectives

- Understand customer purchasing behavior.
- Segment customers using RFM analysis.
- Predict future Customer Lifetime Value.
- Identify Active and At-Risk customers.
- Support business decision-making using data-driven insights.

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Algorithms | K-Means Clustering, Random Forest Regressor |
| Feature Engineering | RFM Analysis, Log Transformation, CLV Engineering |
| Model Evaluation | RMSE, R² Score, MAPE, Cross Validation |
| Development Tools | Jupyter Notebook, Git, GitHub |

---

# 📂 Dataset

The project uses an E-Commerce transaction dataset containing customer purchase history.

### Features Used

- Customer ID
- Invoice Date
- Quantity
- Unit Price
- Total Amount

### Engineered Features

- Recency
- Frequency
- Monetary
- LogFrequency
- LogRecency
- Customer Lifetime Value (CLV)

---

# ⚙️ Project Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
RFM Feature Engineering
      │
      ▼
Customer Segmentation (K-Means)
      │
      ▼
Customer Lifetime Value (CLV) Creation
      │
      ▼
Train-Test Split
      │
      ▼
Random Forest Regression
      │
      ▼
Model Evaluation
      │
      ▼
Business Insights
```
![*]Images/<img width="1009" height="608" alt="image" src="https://github.com/user-attachments/assets/894afa7a-7ba0-4d29-9747-ab4f6815945c" /><img width="1008" height="697" alt="image" src="https://github.com/user-attachments/assets/fb6317aa-ba82-41d6-b0e9-8ad08e873856" /><img width="987" height="737" alt="image" src="https://github.com/user-attachments/assets/22990ec6-88d5-43cc-9d64-bb69c1c6f73e" /><img width="1028" height="760" alt="image" src="https://github.com/user-attachments/assets/52e1a211-e28a-4ed4-bb36-6fe85d75ffda" />




---

# 📊 Exploratory Data Analysis (EDA)

Performed:

- Missing Value Analysis
- Duplicate Removal
- Distribution Analysis
- Correlation Heatmap
- Purchase Distribution
- RFM Visualization

---

# 📈 RFM Analysis

Customer behavior was analyzed using three important business metrics:

### Recency
Days since the customer's last purchase.

### Frequency
Total number of purchases made.

### Monetary
Total amount spent by the customer.

Log transformation was applied to improve model performance.

---

# 👥 Customer Segmentation

K-Means Clustering was used to segment customers into different business groups.

### Customer Segments

- ✅ Active Customers
- ⚠️ At Risk Customers

The quality of clustering was evaluated using the **Silhouette Score**.

---

# 🤖 Machine Learning Model

### Model Used

Random Forest Regressor

### Why Random Forest?

- Handles non-linear relationships
- High prediction accuracy
- Robust against overfitting
- Performs well on business datasets

---

# 📉 Model Evaluation

### Evaluation Metrics

- Root Mean Squared Error (RMSE)
- R² Score
- Mean Absolute Percentage Error (MAPE)

## Final Performance

| Metric | Score |
|---------|-------|
| R² Score | **0.9541** |
| RMSE | **36.58** |
| MAPE | **7.93%** |

---

# ✅ Cross Validation

5-Fold Cross Validation was performed to verify model consistency.

| Metric | Value |
|---------|-------|
| Average Cross Validation RMSE | **35.01** |

The close agreement between Cross Validation RMSE and Test RMSE indicates that the model generalizes well and is not significantly overfitting.

---

# 📊 Visualizations

The project includes:

- Distribution Plots
- Correlation Heatmap
- Customer Segmentation Plot
- Feature Importance Plot
- Actual vs Predicted CLV Plot
- Residual Plot

---

# 🔍 Feature Importance

Random Forest Feature Importance was used to determine the most influential features affecting Customer Lifetime Value.

Important Features:

- Monetary
- Frequency
- Recency
- LogFrequency
- LogRecency

---

# 💰 Predicting Customer Lifetime Value

The trained model predicts Customer Lifetime Value using:

- Recency
- Frequency
- Monetary
- LogFrequency
- LogRecency

Example Prediction

```
Predicted Customer Lifetime Value (CLV): 941.54
```

---

# 📌 Business Insights

## 🟢 Active Customers

- Recently purchased products
- Higher customer engagement
- Suitable for loyalty rewards
- Personalized product recommendations

## 🔴 At Risk Customers

- Long time since last purchase
- Require win-back campaigns
- Personalized discount offers
- Reminder emails and promotional notifications

---

# 📂 Project Structure

```
E-Commerce-CLV-Prediction/

│── data/
│── notebooks/
│── images/
│── models/
│── README.md
│── requirements.txt
│── CLV_Prediction.ipynb
```

---

# 🚀 Future Improvements

- Streamlit Dashboard
- Hyperparameter Tuning (GridSearchCV)
- XGBoost Regression
- SHAP Explainability
- Model Deployment using Flask/FastAPI
- Real-Time CLV Prediction API

---

# 💼 Business Impact

This project enables businesses to:

- Predict Customer Lifetime Value
- Identify valuable customers
- Improve customer retention
- Optimize marketing campaigns
- Increase long-term revenue
- Make data-driven business decisions

---

# 📚 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Customer Analytics
- RFM Analysis
- K-Means Clustering
- Random Forest Regression
- Cross Validation
- Model Evaluation
- Business Intelligence
- Data Visualization
- Machine Learning Pipeline

---

# ⭐ Results

- End-to-End Machine Learning Pipeline
- Customer Segmentation using K-Means Clustering
- Customer Lifetime Value Prediction
- Random Forest Regression Model
- **R² Score: 95.41%**
- **MAPE: 7.93%**
- **RMSE: 36.58**
- **5-Fold Cross Validation RMSE: 35.01**
- Actionable Business Recommendations

---

# 👩‍💻 Author

**Anuska Biswas**

Data Science & Machine Learning Enthusiast

---

## ⭐ If you found this project useful, don't forget to star this repository!
