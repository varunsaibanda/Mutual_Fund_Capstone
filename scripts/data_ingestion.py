import os
import pandas as pd

DATA_PATH = "../data/raw"

for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        file_path = os.path.join(DATA_PATH, file)

        df = pd.read_csv(file_path)

        print("\n" + "=" * 50)
        print(f"FILE: {file}")
        print(f"Shape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())