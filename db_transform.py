import pandas as pd

df = pd.read_csv('/Users/maria/AiCore_Projects/exploratory-data-analysis---customer-loans-in-finance914/loan_payments_data.csv')

# This class converts columns to a more appropriate format
class DataTransform:
    def __init__(self, df):
        self.df = df
    
    def convert_to_int(self, columns):
        for numeric_columns in columns:
            self.df[numeric_columns] = (self.df[numeric_columns].astype('int64', errors='ignore'))
    
    def convert_to_object(self, columns):
        for object_columns in columns:
            self.df[object_columns] = self.df[object_columns].astype('object', errors='ignore')
    
    def convert_to_date(self, columns):
        for date_columns in columns:
            self.df[date_columns] = (self.df[date_columns].apply(pd.to_datetime, format='%b-%y', errors='coerce'))
    
    def convert_to_category(self, columns):
        for category_columns in columns: 
            self.df[category_columns] = self.df[category_columns].astype('category', errors='ignore')
    
    def convert_to_bool(self, columns):
        for bool_columns in columns: 
            self.df[bool_columns] = self.df[bool_columns].map({'y': True, 'n': False})
            self.df[bool_columns] = self.df[bool_columns].astype('bool', errors='ignore')

    def convert_employment_length(self, columns):
        for columns in ['employment_length', 'term']:
            # Extract numeric part from 'X years' format
            self.df[columns] = self.df[columns].str.extract('(\d+)').astype('Int64')
