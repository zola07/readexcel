import pandas as pd
import os
import time
#from datetime import date

start_time = time.process_time()
print("\n")
for root, dirs, files in os.walk("../2018"):
    for filename in files:
      if filename.endswith(".xls") or filename.endswith(".xlsx"):
        xls = pd.ExcelFile(os.path.join(root,filename)) 
        print(xls.sheet_names)
        sheet = pd.read_excel(os.path.join(root,filename),header=None)
        print("\n")
        for k in range(0,sheet.shape[1]):
            if sheet.notnull().iloc[0,k]!=False:
                print(sheet.iloc[0,k],end="  ")
        print("\n")
        for i in range(3,sheet.shape[0]):
            
            for n in range(0,sheet.shape[1]):
                if sheet.notnull().iloc[i,0]!=False and sheet.notnull().iloc[2,n]!=False and sheet.notnull().iloc[i,n]!=False:
                    print(sheet.iloc[i,0],"\n",sheet.iloc[2,n],"\n",sheet.iloc[i,n],end="  ")
                    print("\n")
        print(time.process_time() - start_time, "seconds")  
                    
print(time.process_time() - start_time, "seconds")                      
        # print(sheet.dropna(axis=1,thresh=30))
        # print(sheet.dropna(thresh=14))
        #print(sheet.fillna(''))
        # for i in range(0,sheet.shape[1]):
        #     if  sheet.cell_type(0,i) == 1 :
        #         print(sheet.cell(0,i).value,end=" ")
        #     elif sheet.cell_type(0,i) ==2:
        #         print(int(sheet.cell_value(0, i)),end=" ")
        #     else:
        #             pass    
        # print("\n")
        # for i in range(3,sheet.shape[0]):
        #     print("\n")
        #     for n in range(0,sheet.shape[1]):
        #         if  sheet.cell_type(i,n) ==1:
        #             print(sheet.cell_value(i,n))
        #         elif  sheet.cell_type(i,n) ==2 and sheet.cell_type(2,n)!=3:
        #             print(sheet.cell_value(2,n),int(sheet.cell_value(i,n)))
        #         elif  sheet.cell_type(i,n) ==2 and sheet.cell_type(2,n)==3:
        #             print(date_ex(sheet.cell_value(2,n)),int(sheet.cell_value(i,n)))
        #         else:
        #             pass                
# def date_ex(excel_date):

#     dt = date.fromordinal(date(1900, 1, 1).toordinal() + int(excel_date) - 2)

#     return dt.strftime("%d/%m/%Y")
