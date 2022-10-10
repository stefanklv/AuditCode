# -*- coding: utf-8 -*-
"""
Task 2 Problem 1: Total amount for the AR account in the trial balance is $ 488,671.8. Calculate the sum of 
the AR file and foot it against the AR amount in the trial balance 
"""

import pandas as pd

trial_balance = 488671.8

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I – Kopi.xlsx", usecols="B:K", header=2)

sum_ar = file['bookValue'].sum()

difference = '{:.0f}'.format(sum_ar - trial_balance)

print("The sum of the AR file is " + str(sum_ar) + ", compared to " + str(trial_balance) + 
      " in the trial balance. This makes a difference of " + str(difference))

