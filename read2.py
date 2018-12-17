import os
import time
import pandas as pd

start_time = time.process_time()
listOfFiles = list()
for root, dirs, files in os.walk('../2018'):
    listOfFiles += [os.path.join(root, file) for file in files]
for element in listOfFiles:
    if not element.endswith(('.xls', '.xlsx')):
        continue
    sheet = pd.read_excel(element)
    sheet2 = sheet
    sheet2 = sheet2.loc[:, ~sheet2.columns.str.contains('^Unnamed', na=False)]
    print('--------------------------------------------------\n')
    sheet1 = sheet2.columns.values[:]
    print('  '.join(map(str, sheet1)))
    print("\n")
    for i in range(2, sheet.shape[0]):
        for n in range(1, sheet.shape[1]):
            if sheet.notnull().iloc[1,n] and sheet.notnull().iloc[i,n]:
                print(sheet.iloc[i, 0], "  ", sheet1[0], "  ", sheet.iloc[1, n], "  ", sheet.iloc[i, n], end="  ")
                print("\n")
    print(time.process_time() - start_time, "seconds")

print(time.process_time() - start_time, "seconds")   
