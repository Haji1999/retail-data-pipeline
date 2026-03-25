from pathlib import Path
import logging
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR.parent / 'data' / 'processed' / 'cleaned_retail_data_by_pipeline.csv'

# postgres connection

username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

def load_data_to_postgres():
    logging.info("Starting data load to PostgreSQL")

    # Load cleaned data
    df = pd.read_csv(csv_path)
    logging.info(f"Proccesed CSV loaded succeffully. Shape : {df.shape}")

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

    # Load to PostgreSQL
    df.to_sql('retail_sales', engine, if_exists='replace', index=False)

    logging.info("Data loaded into PostgreSQL successfully")

if __name__=="__main__":
    load_data_to_postgres()