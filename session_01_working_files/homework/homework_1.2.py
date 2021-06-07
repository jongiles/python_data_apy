"""
exercise_1.2.py --
Write function collect_mean_temps(filename) that takes a string filename as argument
and returns list of 'mean_temp' column values from the file. Make sure to convert
each string from the column to an int so we can do some operations on it.
Author: Jon Giles
Last Revised: 6/6/2021
"""
import statistics

def collect_mean_temps(filename):
    mean_temp_readings = []

    fh = open(filename)
    next(fh)

    for line in fh:
        line = line.rstrip()
        fields = line.split(",")
        mean_temp = fields[1]
        i_mean_temp = int(mean_temp)
        mean_temp_readings.append(i_mean_temp)
    return(mean_temp_readings)

file = "../weather_newyork_tiny.csv"
list_of_temps = collect_mean_temps(file)

avg_of_temps = sum(list_of_temps)/len(list_of_temps)

print(list_of_temps)
print(avg_of_temps)
print(statistics.mean(list_of_temps))
print(statistics.median(list_of_temps))
print(statistics.stdev(list_of_temps))
# mean  mean()
# median median()
# standard deviation stdev()