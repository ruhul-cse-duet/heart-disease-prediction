import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os


# Load sample data for feature names
@st.cache_data
def load_sample_data():
    try:
        # Try different possible locations for the dataset
        possible_paths = [
            'dataset/CVD_2021_BRFSS.csv',
            './dataset/CVD_2021_BRFSS.csv'
        ]

        for path in possible_paths:
            if os.path.exists(path):
                df = pd.read_csv(path)
                return df

        raise FileNotFoundError("CVD_2021_BRFSS.csv not found in any expected location")

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

# Enhanced preprocessing function with standard scaling---------------------
def preprocess_input_with_scaling(user_input):
    """
    Prepare a single-row DataFrame for the trained LightGBM model.
    - Drop target column
    - Label-encode categorical features (fitted on sample_df)
    - Keep exact feature order the model was trained on
    """
    df = load_sample_data()
    sample_df = df.copy()
    if sample_df is None or not isinstance(sample_df, pd.DataFrame):
        raise ValueError("sample_df is required and must be a DataFrame")

    # 1) Training-time feature frame (X) = sample_df without target
    if "Heart_Disease" in sample_df.columns:
        X_sample = sample_df.drop(columns=['Heart_Disease'])
    else:
        X_sample = sample_df.copy()

    # 2) Build the single-row input
    user_df = pd.DataFrame([user_input])

    # 3) Categorical columns (object dtype) from X_sample only
    cat_cols = X_sample.select_dtypes(include=["object"]).columns.tolist()

    # 4) Label-encode each categorical col using the mapping from sample data
    for col in cat_cols:
        le = LabelEncoder()
        # fit on sample
        X_sample[col] = X_sample[col].astype(str)
        le.fit(X_sample[col])

        # transform only if user provided that column
        if col in user_df.columns:
            user_df[col] = le.transform(user_df[col].astype(str))
        else:
            mode_val = X_sample[col].mode(dropna=True)
            fill_val = le.transform([str(mode_val.iloc[0])])[0] if not mode_val.empty else 0
            user_df[col] = fill_val

    # 5) Numeric columns → surerity check numeric dtype
    num_cols = [c for c in X_sample.columns if c not in cat_cols]
    for col in num_cols:
        if col in user_df.columns:
            user_df[col] = pd.to_numeric(user_df[col], errors="coerce")
        else:
            user_df[col] = pd.to_numeric(X_sample[col], errors="coerce").median()

    # 6) Missing numeric impute (median)
    for col in num_cols:
        if user_df[col].isna().any():
            user_df[col] = user_df[col].fillna(pd.to_numeric(X_sample[col], errors="coerce").median())

    # 7) Ensure exact training column order
    user_df = user_df[X_sample.columns.tolist()]

    return user_df
