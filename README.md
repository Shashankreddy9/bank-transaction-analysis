# 🏦 Bank Transaction Analysis and Fraud Detection System

An end-to-end data engineering and analytics project that analyses banking transactions, identifies spending patterns, and aims to detect suspicious financial activities using Python, SQL, PySpark, and Machine Learning.

## 🎯 Project Overview

This project simulates a banking transaction analytics pipeline using 10,000 synthetic transaction records.

The goal is to build a data processing system that can:
- Analyse credit and debit transactions.
- Identify customer spending patterns.
- Discover monthly transaction trends.
- Analyse payment methods and spending categories.
- Detect potentially fraudulent transactions.
- Automate data processing workflows.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| MySQL | Database storage and SQL analysis |
| SQLAlchemy | Python-MySQL integration |
| PySpark | Large-scale data processing (planned) |
| Scikit-learn | Machine learning fraud detection (planned) |
| Apache Airflow | Workflow automation (planned) |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
bank-transaction-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── gold/
│
├── src/
│   ├── generate_data.py
│   ├── clean_data.py
│   └── load_mysql.py
│
├── sql/
├── processing/
├── fraud_detection/
├── airflow/
│   └── dags/
├── ai/
├── reports/
│
├── .gitignore
└── README.md
```

## ⚙️ Current Implementation

### 1. Synthetic Data Generation
- Generated 10,000 synthetic banking transactions.
- Included customer IDs, transaction dates, transaction types, amounts, categories, payment modes, and locations.
- Exported the dataset as CSV.

### 2. Data Cleaning
- Removed duplicate transaction IDs.
- Handled missing values.
- Converted transaction dates into datetime format.
- Removed invalid and negative transaction amounts.
- Standardized categorical values.

### 3. MySQL Integration
- Created a MySQL database named `bank_analysis`.
- Created a `bank_transactions` table.
- Loaded 10,000 cleaned transaction records into MySQL using Pandas and SQLAlchemy.

## 📊 Planned SQL Analysis

- Total credit and debit transactions.
- Monthly transaction trends.
- Spending analysis by category.
- Top 10 customers by spending.
- Payment mode analysis.
- High-value transaction identification.
- Customer-level transaction summaries.

## 🚀 Upcoming Features

- Advanced SQL analytics.
- Bronze, Silver, and Gold data architecture.
- PySpark data processing.
- Machine Learning-based fraud detection.
- Anomaly detection.
- Apache Airflow pipeline orchestration.
- AI-powered transaction analysis assistant.

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shashankreddy9/bank-transaction-analysis.git
```

### 2. Navigate into the project

```bash
cd bank-transaction-analysis
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install pandas numpy sqlalchemy pymysql scikit-learn python-dotenv
```

### 6. Configure MySQL

Create the database:

```sql
CREATE DATABASE bank_analysis;
```

Create the `bank_transactions` table using the schema in the project setup.

Configure your local MySQL credentials in `src/load_mysql.py` before running the ingestion script. Never commit real passwords or credentials to GitHub.

### 7. Run the project

Generate synthetic transactions:

```bash
python src/generate_data.py
```

Clean the dataset:

```bash
python src/clean_data.py
```

Load cleaned data into MySQL:

```bash
python src/load_mysql.py
```

## 📌 Project Status

**Currently in development.**

| Component | Status |
|---|---|
| Synthetic data generation | Completed |
| Data cleaning | Completed |
| MySQL integration | Completed |
| SQL analytics | In progress |
| PySpark processing | Planned |
| Fraud detection | Planned |
| Airflow automation | Planned |
| AI assistant | Planned |

## ⚠️ Disclaimer

This project uses synthetic banking transaction data for educational and demonstration purposes. It does not contain real customer banking information and is not intended for actual financial or fraud investigation decisions.

## 👨‍💻 Author

**Shashank Reddy**

GitHub: [@Shashankreddy9](https://github.com/Shashankreddy9)

---

⭐ If you find this project interesting, feel free to explore the repository!