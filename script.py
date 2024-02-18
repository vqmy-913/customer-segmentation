# first python script

# investigate data
import pandas as pd
import csv

purchases = pd.read_csv("data/QVI_purchase_behaviour.csv")
transactions = pd.read_csv("data/QVI_transaction_data.csv")

print(purchases.head())
print(transactions.head())

