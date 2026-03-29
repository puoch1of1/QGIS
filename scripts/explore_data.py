"""
Data Exploration and Preprocessing

Initial exploration of Climate Against Conflict datasets.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from data_loader import load_all_datasets, print_dataset_summary, save_processed_data


def explore_temporal_patterns(df: pd.DataFrame, date_col: str = None) -> None:
    """Analyze temporal patterns in the dataset."""
    print("\nTEMPORAL PATTERNS")
    print("-" * 60)
    
    # Try common date column names
    date_columns = [date_col] if date_col else ['Date', 'Month', 'Year', 'date', 'month', 'year']
    
    for col in date_columns:
        if col in df.columns:
            print(f"Date column found: {col}")
            print(f"Date range: {df[col].min()} to {df[col].max()}")
            break


def explore_geographic_distribution(df: pd.DataFrame) -> None:
    """Analyze geographic distribution in datasets."""
    print("\nGEOGRAPHIC DISTRIBUTION")
    print("-" * 60)
    
    # Look for location columns
    location_cols = [col for col in df.columns if any(term in col.lower() for term in ['state', 'region', 'county', 'location', 'area'])]
    
    if location_cols:
        for col in location_cols:
            print(f"\n{col}:")
            print(f"  Unique locations: {df[col].nunique()}")
            print(f"  Top 5: {df[col].value_counts().head().to_dict()}")


def explore_event_data(df: pd.DataFrame) -> None:
    """Analyze event and fatality statistics."""
    print("\nEVENT & FATALITY STATISTICS")
    print("-" * 60)
    
    # Look for event/fatality columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        if any(term in col.lower() for term in ['event', 'fatality', 'death', 'incident', 'count']):
            print(f"\n{col}:")
            print(f"  Sum: {df[col].sum():,.0f}")
            print(f"  Mean: {df[col].mean():.2f}")
            print(f"  Median: {df[col].median():.2f}")
            print(f"  Max: {df[col].max():.2f}")
            print(f"  Min: {df[col].min():.2f}")
            print(f"  Missing: {df[col].isnull().sum()}")


def check_data_quality(df: pd.DataFrame) -> None:
    """Assess data quality issues."""
    print("\nDATA QUALITY CHECK")
    print("-" * 60)
    
    print(f"Total rows: {len(df)}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print(f"\nMissing values by column:")
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) > 0:
        print(missing)
    else:
        print("  None!")
    
    # Check for potential issues
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        negative_vals = (df[col] < 0).sum()
        if negative_vals > 0:
            print(f"\n  WARNING: {col}: {negative_vals} negative values")


def main():
    print("=" * 70)
    print("CLIMATE AGAINST CONFLICT - DATA EXPLORATION")
    print("=" * 70)
    
    datasets = load_all_datasets()
    
    for name, df in datasets.items():
        print(f"\n\n{'#' * 70}")
        print(f"# {name.upper()}")
        print(f"{'#' * 70}")
        
        print_dataset_summary(df, name)
        explore_temporal_patterns(df)
        explore_geographic_distribution(df)
        explore_event_data(df)
        check_data_quality(df)
    
    print("\n\n" + "=" * 70)
    print("Exploration complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
