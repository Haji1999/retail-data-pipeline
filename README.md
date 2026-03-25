# Retail Data Pipeline (ETL + PostgreSQL + Docker + Airflow)

##  Overview

This project is an end-to-end **Data Engineering pipeline** that processes retail transaction data from a raw Excel dataset into a clean, structured format for analysis.

The pipeline performs:

* Data extraction from Excel
* Data cleaning and transformation
* Loading into PostgreSQL
* Workflow orchestration using Apache Airflow
* Containerization using Docker

---

##  Architecture

Raw Excel → ETL (Python) → Processed CSV → PostgreSQL → Airflow Orchestration → SQL Analytics

---

##  Technologies Used

* Python (pandas)
* PostgreSQL
* SQLAlchemy
* Docker & Docker Compose
* Apache Airflow
* python-dotenv

---

##  Project Structure

```
retail_data_pipeline/
│
├── airflow/
│   ├── dags/
│   │   └── retail_pipeline_dag.py
│   ├── Dockerfile
│   └── requirements-airflow.txt
│
├── data/
│   ├── raw/customer.xlsx
│   └── processed/cleaned_retail_data_by_pipeline.csv
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── load_to_db.py
│   └── run_pipeline.py
│
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

##  Pipeline Workflow

### Step 1: ETL

* Remove duplicates
* Filter invalid data (Quantity ≤ 0, UnitPrice ≤ 0)
* Drop missing CustomerID
* Create Revenue column
* Create Month column

### Step 2: Load

* Load cleaned data into PostgreSQL table `retail_sales`

### Step 3: Orchestration

* Airflow DAG runs:

```
run_etl → load_to_postgres
```

---

##  Running the Project (Docker)

### Build containers

```
docker compose build
```

### Start services

```
docker compose up -d
```

### Open Airflow UI

```
http://localhost:8080
```

### Trigger DAG

* Enable DAG
* Click "Trigger DAG"

---

## 🔍 How to Monitor

* Use **Graph view** in Airflow
* Click tasks → view logs
* Check PostgreSQL for loaded data

---

##  Sample SQL Queries

### Top Customers

```sql
SELECT "CustomerID", SUM("Revenue") AS total_revenue
FROM retail_sales
GROUP BY "CustomerID"
ORDER BY total_revenue DESC
LIMIT 10;
```

---

##  Challenges & Solutions

* Fixed file path issues using pathlib
* Solved Dockerfile extension problem
* Fixed Airflow log error (secret_key)
* Debugged missing script paths in DAG

---

##  Key Skills Demonstrated

* ETL Pipeline Development
* Data Cleaning & Transformation
* SQL & PostgreSQL
* Docker Containerization
* Airflow Orchestration
* Debugging Real-world Issues

---

##  Future Improvements

* Cloud deployment (AWS/GCP)
* API-based ingestion
* Data validation checks
* Dashboard integration

---

## 👨‍💻 Author

Haji – Junior Data Engineer
