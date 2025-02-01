import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from dataset_etl.etl import TitanicETL, TABLE_TITANIC_RAW, TABLE_TITANIC_CLEAN
from pathlib import Path

# Sample test data
ROOT_FOLDER = Path(__file__).parents[1]
TEST_FILE_PATH = ROOT_FOLDER / "test_files/titanic_raw.csv"
EXPECTED_COLS = [
    "PassengerId",
    "Survived",
    "Pclass",
    "Name",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Ticket",
    "Fare",
    "Cabin",
    "Embarked",
]


def test_extract():
    """Test the extract method by mocking pandas read_csv."""

    etl = TitanicETL(file_path=TEST_FILE_PATH)
    df_test = etl.extract()

    assert isinstance(df_test, pd.DataFrame)
    assert not df_test.empty
    for expected_col in EXPECTED_COLS:
        assert expected_col in df_test.columns


def test_transform():
    """Test the transform method to ensure correct cleaning."""
    df_input = pd.read_csv(TEST_FILE_PATH)
    df_transformed = TitanicETL.transform(df_input)

    assert isinstance(df_transformed, pd.DataFrame)
    assert not df_transformed.empty
    assert "Cabin" not in df_transformed.columns  # Ensure column is removed
    assert set(df_transformed.columns) == {"Survived", "Pclass", "Age", "Fare"}


def test_load():
    """Test the load method to ensure correct data transformation."""
    etl = TitanicETL(TEST_FILE_PATH)
    d_data = etl.load()

    assert isinstance(d_data, dict)
    assert TABLE_TITANIC_RAW in d_data
    assert TABLE_TITANIC_CLEAN in d_data
    assert isinstance(d_data[TABLE_TITANIC_CLEAN], pd.DataFrame)
    assert set(d_data[TABLE_TITANIC_CLEAN].columns) == {
        "Survived",
        "Pclass",
        "Age",
        "Fare",
    }
    df_expected = pd.read_csv(ROOT_FOLDER / "test_files/titanic_cleaned.csv")
    assert assert_frame_equal(df_expected, d_data[TABLE_TITANIC_CLEAN])
