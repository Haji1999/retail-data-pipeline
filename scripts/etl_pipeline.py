from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# FILES PATH
BASE_DIR = Path(__file__).resolve().parent
raw_file_path = BASE_DIR.parent / 'data' / 'raw' / 'customer.xlsx'
output_path = BASE_DIR.parent / 'data' / 'processed' / 'cleaned_retail_data_by_pipeline.csv'
output_path.parent.mkdir(parents=True, exist_ok=True)

def run_etl():
    #LOAD
    logging.info("Starting ETL process")
    df = pd.read_excel(raw_file_path)
    logging.info(f"Raw data loaded successfully. Shape : {df.shape}")

    # TRANSFORM
    df = df.drop_duplicates()
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df = df.dropna(subset=['CustomerID'])
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']

    # FEATURE ENGINEERING
    df['Month'] = df['InvoiceDate'].dt.to_period('M')

    logging.info(f"Data transformed successfully. Shape : {df.shape}")

    # SAVE TO CSV
    df.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to {output_path}")



if __name__ == "__main__":
    run_etl()
