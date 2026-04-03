"""
Data Loading Module

Utilities for loading and validating datasets from the Climate Against Conflict project.
"""

import pandas as pd
from pathlib import Path
from typing import Dict


RAW_DATA_DIR = Path(__file__).parent.parent / 'data' / 'raw'
PROCESSED_DATA_DIR = Path(__file__).parent.parent / 'data' / 'processed'
PROJECT_ROOT_DIR = Path(__file__).parent.parent


def _resolve_data_file(filename: str) -> Path:
    """Resolve a dataset filename across expected data locations."""
    candidate_paths = [
        RAW_DATA_DIR / filename,
        PROJECT_ROOT_DIR / filename,
    ]

    for candidate in candidate_paths:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        f"Could not find dataset '{filename}'. Searched: "
        + ", ".join(str(path) for path in candidate_paths)
    )


def _load_excel_dataset(filename: str) -> pd.DataFrame:
    """Load an Excel dataset after resolving its file path."""
    return pd.read_excel(_resolve_data_file(filename))


def load_civilian_targeting() -> pd.DataFrame:
    """Load civilian targeting events and fatalities dataset."""
    return _load_excel_dataset(
        'south-sudan_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx'
    )


def load_political_violence() -> pd.DataFrame:
    """Load political violence events and fatalities dataset."""
    return _load_excel_dataset(
        'south-sudan_hrp_political_violence_events_and_fatalities_by_month-year_as-of-26mar2026.xlsx'
    )


def load_dtm_mobility() -> pd.DataFrame:
    """Load DTM (Displacement Tracking Matrix) mobility dataset."""
    return _load_excel_dataset(
        'ssd-dtm-mobility-tracking-r16-baseline-assessment-dataset_updated_20250507.xlsx'
    )


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
