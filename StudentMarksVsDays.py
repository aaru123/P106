import pandas as pd
import plotly.express as px
import csv
import numpy as np


def getDataSource(data_path):
    marksInPrecentage = []
    daysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            marksInPrecentage.append(float(i['Marks In Percentage']))
            daysPresent.append(float(i['Days Present']))

    return{ 'x': marksInPrecentage, "y": daysPresent}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print("Correlation between marks and days present :- \n--->", correlation[0,1])


def setUp():
    data_path = 'Student Marks vs Days Present.csv'
    
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    
setUp()
