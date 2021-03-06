import os
import time
import datetime
import calendar
import pandas as pd

# start_time = time.process_time()

listOfFiles = list()

for root, dirs, files in os.walk('./2018'):
    listOfFiles += [os.path.join(root, file) for file in files]

for file_path in listOfFiles:
    if not file_path.endswith(('.xls', '.xlsx')):
        continue
    sheet = pd.read_excel(file_path, header=2)
    sheet = sheet.loc[:, ~sheet.columns.str.contains('^Unnamed', na=False)]
    headers = list(sheet.columns.values)[:7]

    week = int(file_path.split('-')[2])

    for date in headers:
        if isinstance(date, str):
            if date[-1] in ['.', '/']:
                date = date[:-1]

            separator = '/'
            if '.' in date:
                separator = '.'

            date = date.replace(f'{separator}{separator}', separator)
            if isinstance(date, str):
                date_list = date.split(separator)
                date_list = date_list[:3]
                try:
                    day = int(date_list[0])
                    month = int(date_list[1])
                    try:
                        year = int(date_list[2])
                    except:
                        year = 2018
                except:
                    print(f'Error {date} on {file_path}. {date_list} separator: {separator}')
                    continue

                try:
                    date_tmp = datetime.date(year, month, day)
                except:

                    try:
                        date_tmp = datetime.date(year, day, month)
                    except:
                        print('Date format error')
                        print(type(date))
                        print(f'Error {date} on {file_path}')
                        continue

        elif isinstance(date, datetime.date):
            date_tmp = date
        else:
            print(type(date))
            raise Exception(f'Error {date} on {file_path}')

        weekNumber = date_tmp.isocalendar()[1]
        if weekNumber not in [week + 1, week, week - 1] :
            print(week, weekNumber)
            print(f'Error {date} on {file_path}')
            continue

















    # if not headers or len(headers) != 7:
    #     print(f'Error on {file_path}')
    #     continue

    # print(headers)
    # break

    # for index, row in sheet.iterrows():
    #     print(row)
    #     break


    # sheet2 = sheet
    # sheet2 = sheet2.loc[:, ~sheet2.columns.str.contains('^Unnamed', na=False)]
    # print('--------------------------------------------------\n')
    # sheet1 = sheet2.columns.values[:]
    # print('  '.join(map(str, sheet1)))
    # print("\n")

    # for index, row in sheet.iterrows():
    #     print(row)

    # for i in range(2, sheet.shape[0]):
    #     for n in range(1, sheet.shape[1]):
    #         if sheet.notnull().iloc[1,n] and sheet.notnull().iloc[i,n]:
    #             print(sheet.iloc[i, 0], "  ", sheet1[0], "  ", sheet.iloc[1, n], "  ", sheet.iloc[i, n], end="  ")
    #             print("\n")

    # print(time.process_time() - start_time, "seconds")

# print(time.process_time() - start_time, "seconds")

