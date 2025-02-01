"""
ETL module for processing the Titanic dataset.

This module defines the TitanicETL class, which performs extract, transform, and load (ETL)
operations on the Titanic dataset.
"""

from typing import Union
import pandas as pd
from pathlib import Path

class TitanicETL:
    """
    A class to handle the ETL process for the Titanic dataset.
    
    Methods:
        extract(file_path): Reads the Titanic dataset from a CSV file.
        transform(df): Cleans and processes the dataset.
        load(df, output_path): Saves the processed dataset to a new CSV file.
    """
    
    @staticmethod
    def extract(file_path: Union[str, Path]) -> pd.DataFrame:
        """Reads the Titanic dataset from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            pd.DataFrame: A DataFrame containing the raw dataset.
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)
        return pd.read_csv(file_path)
    
    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        """Cleans and processes the Titanic dataset.
        
        Args:
            df (pd.DataFrame): Raw Titanic dataset.
            
        Returns:
            pd.DataFrame: Transformed dataset with necessary preprocessing applied.
        """
        df = df.dropna(subset=["Survived", "Pclass", "Age", "Fare"])
        df = df[['Survived', 'Pclass', 'Age', 'Fare']]
        return df
    
    @staticmethod
    def load(df: pd.DataFrame, output_path: str) -> None:
        """Saves the processed dataset to a new CSV file.
        
        Args:
            df (pd.DataFrame): Transformed dataset.
            output_path (str): Path to save the cleaned dataset.
        """
        df.to_csv(output_path, index=False)
