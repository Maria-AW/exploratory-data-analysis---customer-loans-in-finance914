import pandas as pd

df = pd.read_csv('/Users/maria/AiCore_Projects/exploratory-data-analysis---customer-loans-in-finance914/loan_payments_data.csv')

# This class extracts useful information from the DataFrame
class DataFrameInfo:
    def __init__(self, df):
        self.df = df
     
    def describe_columns(self):
        return self.df.dtypes
   
    def extract_stats(self):
        return self.df.describe()
   
    def df_shape(self):
        return self.df.shape
   
    def null_values(self):
        return self.df.isnull().sum()/len(self.df) * 100
   
    def distinct_values(self):
        category_columns = self.df.select_dtypes(include=['category']).columns
        distinct_values ={}
        for column in category_columns:
            distinct_values[column] = self.df[column].unique()
        return distinct_values
    