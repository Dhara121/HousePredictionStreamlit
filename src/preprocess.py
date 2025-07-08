import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def drop_unused_columns(df, cols_to_drop=["Id"]):
    """Drop columns that do not contribute to prediction."""
    return df.drop(columns=cols_to_drop, errors='ignore')


def impute_lot_frontage(df):
    """Impute missing LotFrontage using Neighborhood-wise median."""
    if "LotFrontage" in df.columns and "Neighborhood" in df.columns:
        df["LotFrontage"] = df.groupby("Neighborhood")["LotFrontage"].transform(
            lambda x: x.fillna(x.median())
        )
    return df


def fill_remaining_numerical(df):
    """Fill remaining numeric NaNs with feature-wise median."""
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    return df


def encode_categoricals(df):
    """Label encode categorical columns. Replace missing with 'Missing'."""
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        df[col] = df[col].fillna("Missing")
        df[col] = LabelEncoder().fit_transform(df[col])
    return df


def preprocess_data(df, is_train=True):
    """
    Complete preprocessing pipeline:
    - Drop unused
    - Impute missing
    - Encode categoricals
    - Fill numerics
    """
    df = drop_unused_columns(df)
    df = impute_lot_frontage(df)
    df = fill_remaining_numerical(df)
    df = encode_categoricals(df)

    # Drop rows with missing target only during training
    if is_train and "SalePrice" in df.columns:
        df = df.dropna(subset=["SalePrice"])
    
    return df
