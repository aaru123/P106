import pandas as pd
import plotly.express as px
import csv
import numpy as np


def getDataSource(data_path):
    Coffeeinml = []
    sleepinhours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            Coffeeinml.append(float(i['Coffee in ml']))
            sleepinhours.append(float(i['sleep in hours']))

    return{ 'x': Coffeeinml, "y": sleepinhours}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print("Correlation between coffee Sales and sleep in hours :- \n--->", correlation[0,1])


def setUp():
    data_path = 'cups of coffee vs hours of sleep.csv'
    
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    
setUp()
