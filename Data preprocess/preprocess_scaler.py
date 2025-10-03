import streamlit as st
import pandas as pd

# Feature preparation for scaling
def prepare_features_for_scaling(df):
    """
    Prepare numerical features from the dataset for standard scaling
    """
    try:
        # Create a copy to avoid modifying original
        data = df.copy()

        # Remove target variable if present
        if 'Heart_Disease' in data.columns:
            data = data.drop('Heart_Disease', axis=1)

        # Encode categorical variables first
        from sklearn.preprocessing import LabelEncoder
        categorical_columns = data.select_dtypes(include=['object']).columns

        for col in categorical_columns:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))

        # Get numerical features (including encoded categoricals)
        numerical_features = data.select_dtypes(include=['float64', 'int64', 'int32', 'float32']).fillna(0)

        return numerical_features

    except Exception as e:
        st.error(f"Error preparing features for scaling: {e}")
        return None


# Enhanced preprocessing function with standard scaling---------------------
def preprocess_input_with_scaling(data, sample_df, scaler=None):
    """
    Preprocess input data with proper encoding and standard scaling for LightGBM model
    """
    try:
        processed_data = data.copy()

        # Handle categorical variables based on sample data
        from sklearn.preprocessing import LabelEncoder
        categorical_columns = sample_df.select_dtypes(include=['object']).columns

        # Remove target column from categorical processing
        categorical_columns = [col for col in categorical_columns if col != 'Heart_Disease']

        for col in categorical_columns:
            if col in processed_data:
                # Get unique values from sample data
                unique_values = sample_df[col].unique()
                if processed_data[col] not in unique_values:
                    # Use the most common value as default
                    processed_data[col] = sample_df[col].mode()[0]

                # Encode the categorical variable
                le = LabelEncoder()
                le.fit(sample_df[col].astype(str))
                try:
                    processed_data[col] = le.transform([str(processed_data[col])])[0]
                except:
                    processed_data[col] = 0  # Default for unknown categories

        # Create DataFrame with the processed data
        input_df = pd.DataFrame([processed_data])

        # Ensure all columns from training are present
        training_columns = [col for col in sample_df.columns if col != 'Heart_Disease']
        for col in training_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns to match training data
        input_df = input_df[training_columns]

        # Apply standard scaling if scaler is provided
        if scaler is not None:
            # Only scale numerical features (after encoding)
            numerical_features = input_df.select_dtypes(include=['float64', 'int64', 'int32', 'float32'])

            if len(numerical_features.columns) > 0:
                scaled_features = scaler.transform(numerical_features)
                input_df[numerical_features.columns] = scaled_features

        return input_df

    except Exception as e:
        st.error(f"Error in preprocessing with scaling: {e}")
        return None