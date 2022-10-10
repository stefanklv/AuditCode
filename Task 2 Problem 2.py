# -*- coding: utf-8 -*-
"""
Task 2 Problem 2: Test if there are any duplicates in the file – focus on “invoice number”. Which of these 
duplicates warrant further investigation?
"""

import pandas as pd


file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", usecols="B:K", header=2)

invoice_column = file['invoice number']

duplicate_binary = invoice_column.duplicated()

duplicates = file[invoice_column.isin(invoice_column[duplicate_binary])].sort_values('invoice number')

invoice_numbers = duplicates['invoice number']

print(invoice_numbers)

duplicates_df = duplicates[['invoice number', 'customer number', 'bookValue']]

print(duplicates_df)
