import pandas as pd
import glob

files = glob.glob("*.csv")
count = 0

for file in files:
    df = pd.read_csv(file, dtype=str)
    count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False)).sum().sum()

print(f"Total lines containing 'GitHub': {count}")
