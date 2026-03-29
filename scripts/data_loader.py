"""
Data Loading Module

Utilities for loading and validating datasets from the Climate Against Conflict project.
"""

import pandas as pd
import os
from pathlib import Path
from typing import Dict, Tuple


RAW_DATA_DIR = Path(__file__).parent.parent / 'data' / 'raw'
PROCESSED_DATA_DIR = Path(__file__).parent.parent / 'data' / 'processed'


def load_civilian_targeting() -> pd.DataFrame:
    """Load civilian targeting events and fatalities dataset."""
    file_path = RAW_DATA_DIR / 'south-sudan_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx'
    return pd.read_excel(file_path)


def load_political_violence() -> pd.DataFrame:
    """Load political violence events and fatalities dataset."""
    file_path = RAW_DATA_DIR / 'south-sudan_hrp_political_violence_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx'
    return pd.read_excel(file_path)


def load_dtm_mobility() -> pd.DataFrame:
    """Load DTM (Displacement Tracking Matrix) mobility dataset."""
    file_path = RAW_DATA_DIR / 'ssd-dtm-mobility-tracking-r16-baseline-assessment-dataset_updated_20250507.xlsx'
    return pd.read_excel(file_path)


def load_all_datasets() -> Dict[str, pd.DataFrame]:
    """Load all datasets into a dictionary."""
    datasets = {
        'civilian_targeting': load_civilian_targeting(),
        'political_violence': load_political_violence(),
        'dtm_mobility': load_dtm_mobility(),
    }
    return datasets


def save_processed_data(df: pd.DataFrame, filename: str) -> None:
    """Save processed data to CSV."""
    output_path = PROCESSED_DATA_DIR / filename
    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")


def print_dataset_summary(df: pd.DataFrame, name: str = "Dataset") -> None:
    """Print basic information about a dataset."""
    print(f"\n{'='*60}")
    print(f"{name}")
    print(f"{'='*60}")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nFirst few rows:\n{df.head()}")


if __name__ == "__main__":
    # Test data loading
    print("Loading datasets...")
    datasets = load_all_datasets()
    
    for name, df in datasets.items():
        print_dataset_summary(df, name)
