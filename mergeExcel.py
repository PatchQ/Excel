
import os
import openpyxl
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))

combined = pd.DataFrame()

for filename in os.listdir(dir_path):
    if filename.lower().endswith((".xlsx")):
        df = pd.read_excel(filename, engine="openpyxl", skiprows=3)
        combined = combined.append(df, ignore_index=True)


combined.to_excel("combined.xlsx")


