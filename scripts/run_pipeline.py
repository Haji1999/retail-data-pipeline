import logging
from etl_pipeline import run_etl
from load_to_db import load_data_to_postgres

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Pipeline execution started")
    run_etl()
    load_data_to_postgres()
    logging.info("Pipeline execution completed successfully")

if __name__ == "__main__":
    run_pipeline()
