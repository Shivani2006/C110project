import pandas as pd 
import csv
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv ("newdata.csv")
population_mean = df["average"].mean()
print(population_mean)

std = statistics.stdev(df["average"].tolist())
print(std)

def sampling(ppopulation_data):
    sample_data = []
    for i in range(0,100):
        random_index = random.randint(0,30)
        value = ppopulation_data[random_index]
        sample_data.append(value)
    mean = statistics.mean(sample_data)
    std  = statistics.stdev(sample_data)
    return mean, std



mean_list=[]
for i in range(0,1000):
    sample_mean,sample_std=sampling(df["average"].tolist())
    mean_list.append(sample_mean)
avg = statistics.mean(mean_list)
sd  = statistics.stdev(mean_list)
print(avg,sd)

fig = ff.create_distplot([mean_list],["Average"], show_hist=False)
fig.show()
