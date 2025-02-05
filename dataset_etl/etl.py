"""
ETL module for processing the Titanic dataset.

This module defines the TitanicETL class, which performs extract, transform, and load (ETL)
operations on the Titanic dataset.
"""

from typing import Union, Dict
import pandas as pd
from pathlib import Path

TABLE_TITANIC_RAW: str = "titanic_raw"
TABLE_TITANIC_CLEAN: str = "titanic_clean"


class TitanicETL:
    """
    A class to handle the ETL process for the Titanic dataset.

    Methods:
        extract(file_path): Reads the Titanic dataset from a CSV file.
        transform(df): Cleans and processes the dataset.
        load(df, output_path): Saves the processed dataset to a new CSV file.
    """

    def __init__(self, file_path: Union[str, Path]) -> None:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        self.file_path = file_path

    def extract(self) -> pd.DataFrame:
        """Reads the Titanic dataset from the 'self.file_path'.

        Returns:
            pd.DataFrame: A DataFrame containing the raw dataset.
        """
        return pd.read_csv(self.file_path)

    @staticmethod
    def transform(df: pd.DataFrame) -> pd.DataFrame:
        """Cleans and processes the Titanic dataset.

        Args:
            df (pd.DataFrame): Raw Titanic dataset.

        Returns:
            pd.DataFrame: Transformed dataset with necessary preprocessing applied.
        """
        df = df.dropna(subset=["Survived", "Pclass", "Age", "Fare"])
        df = df[["Survived", "Pclass", "Age", "Fare"]]
        return df

    def load(self) -> Dict[str, pd.DataFrame]:
        """Runs the ETL process to get the clean data from raw titanic dataset in CSV file.

        Return:
            Dict[str, pd.DataFrame]: Dictionary with DataFrames.
        """
        df_raw = self.extract()
        df_clean = self.transform(df=df_raw)
        return {TABLE_TITANIC_RAW: df_raw, TABLE_TITANIC_CLEAN: df_clean}

    @staticmethod
    def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
        """Saves the processed dataset to a new CSV file.

        Args:
            df (pd.DataFrame): Transformed dataset.
            output_path (str): Path to save the cleaned dataset.
        """
        df.to_csv(output_path, index=False)


# Run class using 'test_files/' to do a first check on the code
if __name__ == "__main__":
    root_folder = Path(__file__).parents[1]
    test_file_path = root_folder / "test_files/titanic_raw.csv"

    titanic_etl = TitanicETL(test_file_path)

    d_data = titanic_etl.load()

    titanic_etl.load_to_csv(
        d_data[TABLE_TITANIC_CLEAN], str(root_folder / "test_files/titanic_cleaned.csv")
    )
