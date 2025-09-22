from typing import Any, Union
import pandas as pd
import logging
import seaborn as sns
import matplotlib.pyplot as plt

from .config import *
from . import access

# Set up logging
logger = logging.getLogger(__name__)

"""These are the types of import we might expect in this file
import pandas
import bokeh
import seaborn
import matplotlib.pyplot as plt
import sklearn.decomposition as decomposition
import sklearn.feature_extraction"""

"""Place commands in this file to assess the data you have downloaded.
How are missing values encoded, how are outliers encoded? What do columns represent,
makes rure they are correctly labeled. How is the data indexed. Crete visualisation
routines to assess the data (e.g. in bokeh). Ensure that date formats are correct
and correctly timezoned."""


def data() -> Union[pd.DataFrame, Any]:
    """
    Load the data from access and ensure missing values are correctly encoded as well as
    indices correct, column names informative, date and times correctly formatted.
    Return a structured data structure such as a data frame.

    IMPLEMENTATION GUIDE FOR STUDENTS:
    ==================================

    1. REPLACE THIS FUNCTION WITH YOUR DATA ASSESSMENT CODE:
       - Load data using the access module
       - Check for missing values and handle them appropriately
       - Validate data types and formats
       - Clean and prepare data for analysis

    2. ADD ERROR HANDLING:
       - Handle cases where access.data() returns None
       - Check for data quality issues
       - Validate data structure and content

    3. ADD BASIC LOGGING:
       - Log data quality issues found
       - Log cleaning operations performed
       - Log final data summary

    4. EXAMPLE IMPLEMENTATION:
       df = access.data()
       if df is None:
           print("Error: No data available from access module")
           return None

       print(f"Assessing data quality for {len(df)} rows...")
       # Your data assessment code here
       return df
    """
    logger.info("Starting data assessment")

    # Load data from access module
    df = access.data()

    # Check if data was loaded successfully
    if df is None:
        logger.error("No data available from access module")
        print("Error: Could not load data from access module")
        return None

    logger.info(f"Assessing data quality for {len(df)} rows, {len(df.columns)} columns")

    try:
        # STUDENT IMPLEMENTATION: Add your data assessment code here

        # Example: Check for missing values
        missing_counts = df.isnull().sum()
        if missing_counts.sum() > 0:
            logger.info(f"Found missing values: {missing_counts.to_dict()}")
            print(f"Missing values found: {missing_counts.sum()} total")

        # Example: Check data types
        logger.info(f"Data types: {df.dtypes.to_dict()}")

        # Example: Basic data cleaning (students should customize this)
        # Remove completely empty rows
        df_cleaned = df.dropna(how="all")
        if len(df_cleaned) < len(df):
            logger.info(f"Removed {len(df) - len(df_cleaned)} completely empty rows")

        logger.info(f"Data assessment completed. Final shape: {df_cleaned.shape}")
        return df_cleaned

    except Exception as e:
        logger.error(f"Error during data assessment: {e}")
        print(f"Error assessing data: {e}")
        return None


def query(data: Union[pd.DataFrame, Any]) -> str:
    """Request user input for some aspect of the data."""
    raise NotImplementedError


def view(data: Union[pd.DataFrame, Any]) -> None:
    """Provide a view of the data that allows the user to verify some aspect of its quality."""
    raise NotImplementedError


def labelled(data: Union[pd.DataFrame, Any]) -> Union[pd.DataFrame, Any]:
    """Provide a labelled set of data ready for supervised learning."""
    raise NotImplementedError

def null_values(df):
    print("Missing values per column:\n", df.isna().sum())
    print("\nPercentage missing:\n", (df.isna().mean() * 100).round(2))

def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print(f"Total duplicate rows: {duplicates}")

def statistical_summary(df):
    print("\nStatistical Summary:\n", df.describe())

def info_summary(df):
    print("\nDataset Info:\n", df.info())

def value_counts(df, col):
    print(f"\nValue counts for {col}:\n", df[col].value_counts())
def col_names(df):
    print("\nColumn names:\n", list(df.columns))
    return list(df.columns)
def convert_to_numeric(df):
    numeric_cols = [
        'so2', 'co', 'o3', 'o3_8hr', 'pm10', 'pm2.5',
        'no2', 'nox', 'no', 'windspeed', 'winddirec',
        'co_8hr', 'pm2.5_avg', 'pm10_avg', 'so2_avg'
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    return df

def encode_status(df, col="status"):
    status_mapping = {
        "Good": 0,
        "Moderate": 1,
        "Unhealthy for Sensitive Groups": 2,
        "Unhealthy": 3,
        "Very Unhealthy": 4,
        "Hazardous": 5
    }
    if df[col].dtype == "object":
        df[col] = df[col].map(status_mapping)
    
    return df

def drop_unnecessary_columns(df, cols=None):
    if cols is None:
        cols = [
            'latitude', 'longitude', 'siteid', 'pollutant',
            'sitename', 'county', 'date', 'unit'
        ]
    df = df.drop(columns=cols, errors='ignore')
    return df
    if inplace:
        df.dropna(inplace=True)
        return None
    else:
        return df.dropna()

def encode(df, col="status"):
    mapping = {
        "Good": 0,
        "Moderate": 1,
        "Unhealthy for Sensitive Groups": 2,
        "Unhealthy": 3,
        "Very Unhealthy": 4,
        "Hazardous": 5
    }
    df[col] = df[col].map(mapping)
    return df
def correlation_matrix(df, figsize=(12, 8), cmap="coolwarm"):
    corr = df.corr(numeric_only=True)
    
    # Plot heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap, cbar=True, square=True)
    plt.title("Correlation Matrix", fontsize=16)
    plt.show()
    
    return corr
