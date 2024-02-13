import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


data = pd.read_csv('adult.data', header=None)
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
                'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data.columns = column_names


# Replace "?" with NaN
data = data.applymap(lambda x: np.nan if x == " ?" else x)

# # Handle missing values using imputation
imputer = SimpleImputer(strategy='most_frequent')
data[column_names] = imputer.fit_transform(data[column_names])


# Drop the "fnlwgt" column as it's not a useful predictor
data.drop(['fnlwgt'], axis=1, inplace=True)

# # Encode categorical variables
categorical_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'native-country']
data_encoded = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# # Scale numerical features
# numerical_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
# scaler = StandardScaler()
# data_encoded[numerical_cols] = scaler.fit_transform(data_encoded[numerical_cols])


# Save the cleaned dataset to a new file
data_encoded.to_csv('adult_clean.csv', index=False)