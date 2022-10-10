# -*- coding: utf-8 -*-
"""
Task 3 Problem 4: Roger Company has a policy that their allowance for 
uncollectible accounts should be 50% of the amount in the 60-90 day past 
due category plus 75% of the amount in the >90 day past due category as of 
the reporting date (in this case December 31. Use the Roger Company’s AR table 
to re-compute the allowance for uncollectible accounts. In addition to re-computing 
the allowance for uncollectible accounts, report the results of the aging table 
that you are asked to complete.
"""

import pandas as pd
from datetime import datetime 

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", 
                     usecols="B:K", header=2)

file_ordered = file[['invoice number', 'bookValue', 'due date']]

balance_date_obj = datetime.strptime('2011-12-31 00:00:00', '%Y-%m-%d %H:%M:%S')

sixty_to_ninety_sum = 0
ninety_plus_sum = 0


for i in file_ordered.index: 
    time_difference = balance_date_obj - file_ordered['due date'][i]
    if int(time_difference.days) > 60 and time_difference.days < 90:
        sixty_to_ninety_sum += file_ordered['bookValue'][i]
    elif int(time_difference.days) > 90: 
        ninety_plus_sum += file_ordered['bookValue'][i]

allowance_sixty_to_ninety = sixty_to_ninety_sum * 0.5
allowance_ninety_plus = ninety_plus_sum * 0.75
          
total_allowance = allowance_sixty_to_ninety + allowance_ninety_plus 



print("Total allowance for uncollectable amounts: " + '{:.0f}'.format(total_allowance))

print('60-90 days overdue: ' + '{:.0f}'.format(sixty_to_ninety_sum))
print('90+ days overdue: ' + '{:.0f}'.format(ninety_plus_sum))



