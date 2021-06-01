import plotly.figure_factory as gx
import plotly.graph_objects as fx
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv") #yuhhhh
data = df["time"].tolist() #hello teacher are you proud that i am doing my projects :]

def meansetrandom(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = gx.create_distplot([df], ["time"], show_hist = False)
    fig.add_trace(fx.scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    meanlist = []
    for i in range(0, 1000):
        meanset = meansetrandom(100)
        meanlist.append(meanset)
    show_fig(meanlist)
    
    mean = statistics.mean(meanlist)
    print("mean of sampling distribution: ", mean)

setup()

population_mean = statistics.mean(data)
print("population mean: ", population_mean)

def sdev():
    meanlist = []
    for i in range(0,1000):
        meanset = meansetrandom(100)
        meanlist.append(meanset)

    sd = statistics.stdev(meanlist)
    print("sampling mean: ", sd)

sdev()