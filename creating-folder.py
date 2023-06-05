import os
import openpyxl

RESULT_LOCATION = "C://Users/CMR/OneDrive/Desktop/DORI Website/July2022_batch"
DATA = "C://Users/CMR/OneDrive/Desktop/application.xlsx"


workbook = openpyxl.load_workbook(DATA)
sheet = workbook['Sheet1']

column_values = [cell.value for col in sheet.iter_cols(
    min_row=2, max_row=None, min_col=2, max_col=2) for cell in col]

#for value in column_values:
#    print("Creating folder: ", value)

for value in column_values:
    folderName = value
    baseDir = RESULT_LOCATION
    os.makedirs(os.path.join(baseDir, folderName))
    #print("Created folder: ", folderName)
print("all folders created successfully")
