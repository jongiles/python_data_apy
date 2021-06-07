"""
exercise_1.3.py --
FBuilding a set from a file. Write a function collect_unique(filename) that takes a filename argument
and collects a set of unique words from the file (our test will read from sonnet_xv_tiny.txt).
The words must be lowercased and stripped of punctuation before being added to the set.
Finally the function returns a sorted list of these unique words.
Author: Jon Giles
Last Revised: 6/6s/2021
"""

def collect_unique(filename):
    fh = open(file)
    next(fh)

    mean_temp_readings = []

    for line in fh:
        line = line.rstrip()
        fields = line.split(",")
        mean_temp = fields[1]
        f_mean_temp = float(mean_temp)
        mean_temp_readings.append(f_mean_temp)
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