# test_setup.py
import sys
print(f"Python version: {sys.version}")

import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn as sns
import imblearn
import optuna

print("\n✅ All packages installed successfully!")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print(f"Imbalanced-learn: {imblearn.__version__}")
print(f"Optuna: {optuna.__version__}")

# Test dataset loading
try:
    df = pd.read_csv('data/CDC_Diabetes_Dataset.csv')
    print(f"\n✅ Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
except Exception as e:
    print(f"\n❌ Error loading dataset: {e}")