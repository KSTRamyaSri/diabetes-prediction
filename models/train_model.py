import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
# Make sure the path matches your folder

df = pd.read_csv('../data/diabetes.csv')

# Prepare features and label (assuming 'Outcome' is target)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale (standardize) features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Optionally, print accuracy
print('Accuracy:', model.score(X_test_scaled, y_test))

# Save model and scaler as .pkl files
import os
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/diabetes_rf.pkl')
joblib.dump(scaler, 'models/diabetes_scaler.pkl')
print('Model and scaler saved.')
