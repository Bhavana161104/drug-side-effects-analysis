# 💊 Drug Side Effects Analysis

## 📌 Project Overview
This project analyzes drug-related data and predicts sentiment (Positive, Neutral, Negative) using machine learning. The goal is to identify potential side effects and understand user satisfaction based on available features.

---

## 🎯 Problem Statement
To analyze drug data and classify sentiment using existing features, helping identify drugs that may have potential side effects and improving decision-making in healthcare.

---

## 📂 Dataset
- Source: Kaggle (Drug Review Dataset - processed version)
- Features used:
  - `drug_name`
  - `condition`
  - `nltkRScore` (sentiment score)
  - `useful_count_encoded`

---

## ⚙️ Project Workflow

### 1. Data Collection
- Loaded dataset from CSV file

### 2. Data Preprocessing
- Removed missing values
- Created sentiment labels using quantile-based binning

### 3. Exploratory Data Analysis (EDA)
- Visualized sentiment distribution
- Analyzed top medical conditions

### 4. Feature Engineering
- Encoded categorical variable (`condition`)
- Selected relevant features for modeling

### 5. Model Building
- Random Forest Classifier
- Logistic Regression

### 6. Model Evaluation
- Accuracy Score
- Classification Report
- Confusion Matrix

---

## 🤖 Models Used
- Random Forest Classifier
- Logistic Regression

---

## 📊 Results
- Successfully classified sentiment into:
  - Positive
  - Neutral
  - Negative
- Models achieved good accuracy on test data
- Identified drugs with higher negative sentiment (possible side effects)

---

## 💡 Key Insights
- Some drugs show higher negative sentiment, indicating possible side effects
- Condition plays an important role in drug effectiveness
- Useful count reflects user trust and engagement

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Pickle (for model saving)

---

## 📁 Project Structure
