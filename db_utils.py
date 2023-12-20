import yaml
from sqlalchemy import create_engine
import pandas as pd

# Function to load credentials from credentials.yaml
def load_credentials():
    with open ("/Users/maria/AiCore_Projects/exploratory-data-analysis---customer-loans-in-finance914/credentials.yaml", "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector: 
    def __init__ (self, credentials):
        self.credentials = credentials

    # Extracting credentials   
    def extract_credentials(self):
        host = self.credentials['RDS_HOST']
        user = self.credentials['RDS_USER']
        password = self.credentials['RDS_PASSWORD']
        database = self.credentials['RDS_DATABASE']
        port = self.credentials['RDS_PORT']

        # Creating SQLAlchemy engine
        engine_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(engine_str)
        return engine
    
    # Extracting data
    def extract_data(self, loan_payments):
        extract_cred = self.extract_credentials()
        query = f"SELECT * FROM loan_payments"
        df = pd.read_sql(query, extract_cred)
        return df
    
    def save_data_csv(self, df, csv_file="loan_payments_data.csv"):
        df.to_csv(csv_file, index=False)

# Load Credentials
credentials = load_credentials()
# Initialise RDSDatabaseConnector
rds_connector = RDSDatabaseConnector(credentials)
# Extract data
data = rds_connector.extract_data('loan_payments')
# Save to CSV
rds_connector.save_data_csv(data, 'loan_payments_data.csv')