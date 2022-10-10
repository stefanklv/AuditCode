# -*- coding: utf-8 -*-
"""
Task 3 Problem 1: A normal inbuilt control in an IT-based system would be that an invoice cannot be sent unless 
the invoice date is before the due date. Test if this is the case in Roger Company.
"""

import pandas as pd

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", 
                     usecols="B:K", header=2)

'The control can be tested by checking if there are any records where invoice date > due date'

invoice_column = file['invoice number']
invoice_date = file['invoice date']
due_date = file['due date']

control_failures = file[file['invoice date'] > file['due date']]
control_failures_ordered = control_failures[['invoice number', 'invoice date', 'due date']]

count_control_failures = control_failures['invoice number'].count()

print(control_failures_ordered)
print(count_control_failures)

