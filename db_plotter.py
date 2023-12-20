import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.graphics.gofplots import qqplot
import statsmodels.api as sm
import missingno as msno

df = pd.read_csv('/Users/maria/AiCore_Projects/exploratory-data-analysis---customer-loans-in-finance914/loan_payments_data.csv')

class Plotter: 
    @staticmethod
    def null_heatmap(df):
        msno.heatmap(df)
    
    @staticmethod
    def null_matrix(df):
        msno.matrix(df)

    @staticmethod
    def plot_distribution(df, column):
        plt.title(f'Distribution of {column}')
        df[column].hist(bins=50)
        plt.show()
    
    @staticmethod
    def qq_plot(df_dropped_cols, skewed_columns, transformation_func):
        transformed_values = df_dropped_cols[skewed_columns].apply(transformation_func)
        sm.qqplot(transformed_values, scale=1, line='q', fit=False)
        plt.title(f'QQ Plot for {skewed_columns}')
        plt.show()

    @staticmethod
    def scatter_plot(df_dropped_cols, skewed_columns, transformation_func):
        transformed_values = df_dropped_cols[skewed_columns].apply(lambda x: transformation_func(x))

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df_dropped_cols[skewed_columns], y=transformed_values)
        plt.title(f'Scatter Plot for {skewed_columns}')
        plt.xlabel(skewed_columns)
        plt.ylabel(f'Transformed {skewed_columns}')
        plt.show()

    @staticmethod
    def visualise_correlation(df_without_outliers):
        # Select only numeric columns
        numeric_cols = df_without_outliers.select_dtypes(include=['float64', 'int64']).columns
        df_numeric = df_without_outliers[numeric_cols]  
       
        corr_matrix = df_numeric.corr()
       
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title("Correlation Matrix")
        plt.show()

    @staticmethod
    def identify_highly_correlated(df_without_outliers, threshold=0.8):
        # Select only numeric columns
        numeric_cols = df_without_outliers.select_dtypes(include=['float64', 'int64']).columns
        df_numeric = df_without_outliers[numeric_cols]  
       
        corr_matrix = df_numeric.corr().abs()
        
        upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        
        # Select columns with correlation above the threshold
        high_correlated_cols = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]
        return high_correlated_cols
