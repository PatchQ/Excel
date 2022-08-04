import os
import openpyxl

dir_path = os.path.dirname(os.path.realpath(__file__))

values = []

for filename in os.listdir(dir_path):
    if filename.lower().endswith((".xlsx")):

        wb = openpyxl.load_workbook(filename)
        sheet = wb["Sheet1"]
        value = sheet["C10"].value
        values.append(value)
        
print(values)

