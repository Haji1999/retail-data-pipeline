from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'haji'
}

with DAG(
    dag_id ="retail_data_pipeline_dag",
    default_args=default_args,
    start_date=datetime(2026,3,1),
    schedule_interval="@daily",
    catchup=False,
    tags=["data_engineering", "retail"]
) as dag:
    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="python /app/scripts/etl_pipeline.py",
    )

    load_to_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /app/scripts/load_to_db.py",
    )

    run_etl >> load_to_postgres