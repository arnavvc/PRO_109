import csv
import pandas as bear
import plotly.figure_factory as ff
import statistics as stats

# SOME OF THE LISTNAMES:
# math score
# reading score
# writing score

df = bear.read_csv("StudentsPerformance.csv")
listname = str(input("Enter the list name: "))
dflist = df[listname].tolist()

mean = stats.mean(dflist)
median = stats.median(dflist)
mode = stats.mode(dflist)
stdev = stats.stdev(dflist)

print("\n")
print(f"Mean of {listname} is {mean}.")
print(f"Median of {listname} is {median}.")
print(f"Mode of {listname} is {mode}.")
print(f"Standard Deviation of {listname} is {stdev}.")
print("\n")

stdev_start_1, stdev_end_1 = mean-stdev, mean+stdev
stdev_start_2, stdev_end_2 = mean-2*stdev, mean+2*stdev
stdev_start_3, stdev_end_3 = mean-3*stdev, mean+3*stdev

data_within_stdev_1 = [result for result in dflist if result > stdev_start_1 and result < stdev_end_1]
data_within_stdev_2 = [result for result in dflist if result > stdev_start_2 and result < stdev_end_2]
data_within_stdev_3 = [result for result in dflist if result > stdev_start_3 and result < stdev_end_3]

print(f"{len(data_within_stdev_1)*100.0/len(dflist)}% of data for {listname} lies within the 1st Standard Deviation.")
print(f"{len(data_within_stdev_2)*100.0/len(dflist)}% of data for {listname} lies within the 2nd Standard Deviation.")
print(f"{len(data_within_stdev_3)*100.0/len(dflist)}% of data for {listname} lies within the 3rd Standard Deviation.")
print("\n")