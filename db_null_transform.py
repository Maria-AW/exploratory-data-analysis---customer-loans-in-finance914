import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
from sklearn.preprocessing import PowerTransformer
from scipy.stats import zscore

df = pd.read_csv('/Users/maria/AiCore_Projects/exploratory-data-analysis---customer-loans-in-finance914/loan_payments_data.csv')

class DataFrameTransform: 
    @staticmethod
    def check_nulls(df):
        return df.isnull().sum()/len(df) * 100 
    
    @staticmethod
    def drop_columns(df, columns_to_drop):
        df_drop = df.drop(columns=columns_to_drop)
        return df_drop 
    
    @staticmethod
    def impute_missing_values(df, columns_to_impute, method='median'):
        if method == 'median':
            df[columns_to_impute] = df[columns_to_impute].fillna(df[columns_to_impute].median())
            return df
    
    @staticmethod
    def visualise_original_distribution(df, skewed_columns):
        sns.histplot(df[skewed_columns], label="Original Distribution", kde=True)
        plt.legend()
        plt.show()

    @staticmethod
    def visualise_transformed_distribution(df_dropped_cols, skewed_columns, transformation_func):
        transformed_values = transformation_func(df_dropped_cols[skewed_columns])
        sns.histplot(transformed_values, bins=20, label="Transformed Distribution", kde=False)
        plt.legend()
        plt.show()

    @staticmethod
    def qq_plot(df_dropped_cols, skewed_columns, transformation_func):
        transformed_values = transformation_func(df_dropped_cols[skewed_columns])
        qq_plot = qqplot(transformed_values, scale=1, line='q', fit=False)
        plt.show()

    @staticmethod
    def compare_skewness(df_dropped_cols, skewed_columns):
        original_skewness = df_dropped_cols[skewed_columns].skew()
        df_transformed = DataFrameTransform.apply_boxcox_transformation(df_dropped_cols.copy(), skewed_columns)
        transformed_skewness = df_transformed[skewed_columns].skew()

        print(f"Original Skewness for {skewed_columns}: {original_skewness:.2f}")
        print(f"Transformed Skewness for {skewed_columns}: {transformed_skewness:.2f}")

    @staticmethod
    def apply_boxcox_transformation(df_dropped_cols, columns_to_transform):
        # Check for constant columns
        constant_columns = df_dropped_cols[columns_to_transform].columns[df_dropped_cols[columns_to_transform].nunique() == 1]
        
        # Remove constant columns from the list of columns to transform
        columns_to_transform = [col for col in columns_to_transform if col not in constant_columns]
        
        if columns_to_transform:
            # Ensuring remaining data is positive
            df_dropped_cols[columns_to_transform] += 1e-10
            # Initialise PowerTransformer
            pt = PowerTransformer(method='box-cox')
            # Fit and transform the selected columns 
            df_dropped_cols[columns_to_transform] = pt.fit_transform(df_dropped_cols[columns_to_transform])
        return df_dropped_cols

    @staticmethod
    def apply_log_transformation(df_dropped_cols, skewed_columns):
        return df_dropped_cols[skewed_columns].map(lambda x: np.log(x) if x > 0 else 0)
    
    @staticmethod
    def zscore_outliers(df_dropped_cols, threshold=3):
        numeric_columns = df_dropped_cols.select_dtypes(include=['float64', 'int64']).columns
        df_numeric = df_dropped_cols[numeric_columns]
        z_scores = zscore(df_numeric)
        # Replace vaulues in df_numeric with Z-scores 
        df_numeric[df_numeric.columns] = z_scores
        # Identifying outliers
        z_score_outlier = (df_numeric > threshold) | (df_numeric < -threshold)
        non_outliers_df = df_dropped_cols[~z_score_outlier.any(axis=1)]
        return non_outliers_df