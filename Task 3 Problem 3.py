# -*- coding: utf-8 -*-
"""
Task 3 Problem 3: Possible misstatements that may occur during the cash receipts
process result from cash receipts being received, but not recorded 
(which could facilitate embezzlement). A control technique that 
is used to mitigate the risk of such misstatements is to segregate the duties of 
the accounts receivable department, general ledger accounting records, 
and cash receipts. The employee who completed each duty is required to sign 
his/her initials, and evidence of this has been provided for you in the AR table. 
In each transaction, proper segregation of duties is accomplished when 
no two duties have been completed by the same person. Use the information from Roger 
Company’s AR table to determine in which transactions segregation of duties was not properly 
implemented.
"""

import pandas as pd

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", 
                     usecols="B:K", header=2)


duty_segregation_failure = file[(file['cash receipts clerk'] == file['GL accounting']) | 
                                (file['ar clerk'] == file['cash receipts clerk']) | 
                                (file['GL accounting'] == file['cash receipts clerk'])]

duty_segregation_failure_clean = duty_segregation_failure[['invoice number', 'bookValue', 
                                                           'ar clerk',
                                                           'cash receipts clerk', 
                                                           'GL accounting']]

print(duty_segregation_failure_clean)
