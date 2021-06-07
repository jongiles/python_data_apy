"""
exercise_1.1.py --
File looping and summing. Sum up the price values from each line of ad_buys.csv.
(For this solution, please do not use the CSV module.)
Print each price as you loop, then show the sum, rounded to 2 places.
Author: Jon Giles
Last Revised: 6/4/2021
"""

file = "../ad_buys.csv"

fh = open(file)
next(fh)

totals_prices = 0

for line in fh:
    line = line.rstrip()
    ad_buy_fields = line.split(",")
    price = ad_buy_fields[4]
    buyer_id = ad_buy_fields[1]
    if buyer_id == '1':
        fprice = float(price)
        print(fprice)
        totals_prices = totals_prices + fprice

print(f"sum: {totals_prices}")