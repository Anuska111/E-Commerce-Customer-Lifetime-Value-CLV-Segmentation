
# 📊 E-Commerce Customer Lifetime Value (CLV) Prediction & Customer Segmentation

> An end-to-end Machine Learning project that predicts Customer Lifetime Value (CLV) and segments customers using RFM Analysis, K-Means Clustering, and Random Forest Regression to help businesses improve customer retention and maximize revenue.

---
<img width="1075" height="791" alt="image" src="https://github.com/user-attachments/assets/c4d39078-7fc0-4e2d-9632-e3797c5e0c6a" />


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
<h2 align="center">📷 Project Screenshots</h2>
<img width="1080" height="971" alt="image" src="https://github.com/user-attachments/assets/31d172ff-a11d-4404-b92d-dab57f37fe4f" /><img width="1070" height="629" alt="image" src="https://github.com/user-attachments/assets/d672e74f-de2d-4b80-b2a2-da28d15a2003" /><img width="1071" height="737" alt="image" src="https://github.com/user-attachments/assets/ee0e3d9a-4fad-47d3-9f0b-0c7edb930147" /><img width="1075" height="727" alt="image" src="https://github.com/user-attachments/assets/e3c3070f-376e-4229-83fe-f57976d167e1" /><img width="1080" height="758" alt="image" src="https://github.com/user-attachments/assets/e53aec93-23c2-494e-8b7e-b0b96e6994f3" />
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
| R² Score | **0.973** |
| RMSE | **24.590** |
| MAPE | **7.448%** |

---

# ✅ Cross Validation

5-Fold Cross Validation was performed to verify model consistency.

| Metric | Value |
|---------|-------|
| Average Cross Validation RMSE | **27.748** |

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

## 🚀 Live Demo

👉 **Try the live Streamlit application here:**

**https://e-commerce-customer-lifetime-value-clv-segmentation-mzpwvzvybp.streamlit.app/**
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
- **R² Score: 97.31%**
- **MAPE: 7.45%**
- **RMSE: 24.59**
- **5-Fold Cross Validation RMSE: 27.75**
- Actionable Business Recommendations

---

# 👩‍💻 Author

**Anuska Biswas**

Data Science & Machine Learning Enthusiast

---

## ⭐ If you found this project useful, don't forget to star this repository!
