import pandas as pd

def load_data(path="data/molecular_lines.csv"):
    df = pd.read_csv(path)
    return df
