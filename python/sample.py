import numpy as np
import pandas as pd

def hello():
    return "world"

def meanage(filename):
    # Read data
    titanic = pd.read_csv(filename,",")

    # Set passenger ages to a NumPy array
    passenger_ages = titanic['Age']
    #print(passenger_ages)

    # Use numpy to calculate the mean age of passengers
    mean_age = np.nanmean(passenger_ages)

    #print(mean_age)

    return str(mean_age)

print(meanage("/irisrun/repo/data/titanic.csv"))
