# Example of automated ETL pipeline
Sample repo on how to implement an automated ETL pipeline with python and github actions
This repository contains a sample ETL (Extract, Transform, Load) pipeline implemented as a Python package, where its release is automated using github actions. This automation is useful for CI life-cycle of ETL process.

## Features
- **Extract:** Reads raw data from a CSV file.
- **Transform:** Cleans missing values, drops unnecessary columns, and creates new features.
- **Load:** Returns the transformed dataset as DataFrame, where user can save it as new CSV file if necessary.

## Dataset
The dataset used is the Titanic dataset from Kaggle. You can download it from [Kaggle - Titanic Dataset](https://www.kaggle.com/competitions/titanic/data). Rename `train.csv` to `titanic_raw.csv` and place it in the working directory.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/titanic-etl.git
   cd titanic-etl
   ```
2. Install the package:
   ```bash
   pip install .
   ```

## Usage
Example usage in Python:
```python
from titanic_etl import TitanicETL

etl = TitanicETL(input_path="data/titanic_raw.csv", output_path="data/titanic_cleaned.csv")
etl.run_pipeline()
```

## Project Structure
```
├── titanic_etl          # Python package directory
│   ├── __init__.py      # Package initialization
│   ├── etl.py           # ETL pipeline script
├── data                 # Data directory (ignored in .gitignore)
│   ├── titanic_raw.csv  # Input raw dataset (downloaded from Kaggle)
│   ├── titanic_cleaned.csv  # Output cleaned dataset
├── setup.py             # Package setup script
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
```

## License
This project is open-source under the MIT License.

---

Feel free to modify the pipeline for other datasets! 🚀