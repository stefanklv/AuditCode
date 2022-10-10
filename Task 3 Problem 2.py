# -*- coding: utf-8 -*-
"""
Task 3 Problem 2: Possible misstatements due to lack of appropriate sales authorization 
include selling goods at unauthorized prices, selling amounts that exceed 
customer credit limits, and/or selling to customers who are bad credit risks. 
Roger Company’s policy does permit sales in excess of credit limits, 
but only with management approval.  
"""

import pandas as pd

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", 
                     usecols="B:K", header=2)

""" a) Use the Roger Company’s AR table to determine how many sales were made that 
exceeded customer credit limits. """

excess_records = file[file['bookValue'] > file['credit limit']]
excess_records_clean = excess_records[['invoice number', 'bookValue', 'credit limit']]
excess_records_count = excess_records_clean['invoice number'].count() 

print(excess_records_clean) 
print(excess_records_count)

""" b) Determine how many of the sales in part "a" (where the credit limit was surpassed) that 
were not approved. """ 

excess_without_approval = excess_records[excess_records['authorized'] == 'No']
excess_without_approval_clean = excess_without_approval[['invoice number', 
                                                         'authorized', 'bookValue', 
                                                         'credit limit']]
excess_without_approval_count = excess_without_approval['invoice number'].count()

print(excess_without_approval_clean) 
print(excess_without_approval_count)

