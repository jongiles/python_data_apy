"""Building a dict lookup from file. Write a function get_lookup(filename)
that builds a "lookup dict" of company tickers to company names from nyse-listed_csv_tiny.csv.
(The program should use the csv module because the data has commas in it.)
"""

import csv

def get_lookup(filename):
    fh = open(filename)
    reader = csv.reader(fh)

    ticker_name = {}

    for row in reader:
        ticker_name[row[0]] = row[1]

    return ticker_name


file = "../nyse-listed_csv_tiny.csv"

tickers_and_names = get_lookup(file)
print(tickers_and_names)