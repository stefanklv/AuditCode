# -*- coding: utf-8 -*-
"""
Task 3 Problem 5: After reviewing a list of parties related to Roger Company, 
you notice that the customers with customer numbers 803882 and 512198 are 
related to the owners of the company. Please use the Roger Company’s AR table 
to determine the amount of accounts receivable that relates to sales 
made to these related-party customers. What percent of total accounts receivable are made up of 
sales to these two related-party customers?
"""

import pandas as pd

file = pd.read_excel(r"C:\Users\stefa\OneDrive\Skrivebord\Roger_Company_AR_I.xlsx", 
                     usecols="B:K", header=2)

ordered_file = file[['customer number','invoice number', 'bookValue']]

related_customer_numbers = [803882,512198]

related_transactions_df = ordered_file[ordered_file['customer number'].isin(related_customer_numbers)]
related_transactions_sum = related_transactions_df['bookValue'].sum()

total_sum = ordered_file['bookValue'].sum()
related_transactions_share = '{:.2f}'.format(related_transactions_sum / total_sum * 100)


print("Value of AR of related-parties: " + str(related_transactions_sum))
print("AR of related-parties as % of total sum: " + str(related_transactions_share) + "%")



