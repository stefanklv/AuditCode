# -*- coding: utf-8 -*-
"""
Task 2 Problem 3: Test if there are any omissions in the file – focus on “invoice number"
"""

import pandas as pd

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I – Kopi.xlsx", 
                     usecols="B:K", header=2)

invoice_column = file['invoice number']

range_invoice_numbers = [i for i in range(file['invoice number'][0],file['invoice number'].iloc[-1]+1)]

invoice_column_list = invoice_column.tolist()

omissions = []


for i in range_invoice_numbers: 
    if i not in invoice_column_list: 
        omissions.append(i)

print(omissions)

if omissions == []: 
    print("There are no omissions in the file.")
