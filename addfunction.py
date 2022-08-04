import os
import openpyxl

dir_path = os.path.dirname(os.path.realpath(__file__))

values = []

for filename in os.listdir(dir_path):
    if filename.lower().endswith((".xlsx")):

        wb = openpyxl.load_workbook(filename)
        sheet = wb["Sheet1"]
        sheet["B28"] = "=SUM(B1:B27)"
        # sheet["B28"].style = "Currency"
        wb.save(filename)
    


