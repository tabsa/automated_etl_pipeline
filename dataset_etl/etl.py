import pandas as pd
import os

class TitanicETL:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def extract(self) -> pd.DataFrame:
        """Extract raw data from CSV."""
        return pd.read_csv(self.input_path)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform data: handle missing values, convert types, and create new features."""
        df = df.drop(columns=['Cabin'], errors='ignore')  # Drop 'Cabin' due to many missing values
        df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing Age with median
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing Embarked with mode
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # Create new feature
        return df

    def load(self, df: pd.DataFrame):
        """Load transformed data to CSV."""
        df.to_csv(self.output_path, index=False)

    def run_pipeline(self):
        """Run the full ETL pipeline."""
        print("Extracting data...")
        data = self.extract()
        print("Transforming data...")
        transformed_data = self.transform(data)
        print("Loading data...")
        self.load(transformed_data)
        print("ETL pipeline completed successfully!")
