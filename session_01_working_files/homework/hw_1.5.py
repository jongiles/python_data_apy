"""
Writing rows with selected columns. Read weather_newyork_tiny.csv and build a new CSV file,
weather_newyork_narrow.csv with only the following columns: date, mean_temp, precip, events.
Please use the csv module for this solution.
When complete, weather_newyork_narrow.csv should have the following text
(note that the events column value ('Rain', 'Fog-Rain', etc.) is sometimes missing):
"""

import csv

in_file = "../weather_newyork_tiny.csv"
out_file = "../weather_newyork_narrow.csv"

new_lines = []

fh = open(in_file)
reader = csv.reader(fh)
header_row = next(reader)

wfh = open(out_file, 'w', newline='')
writer = csv.writer(wfh)

new_lines.append(['date', 'mean_temp', 'precip', 'events'])

for row in reader:
    date, mean_temp = row[0:2]
    precip = row[-4]
    events = row[-2]
    new_lines.append([date, mean_temp, precip, events])

writer.writerows(new_lines)
wfh.close()

