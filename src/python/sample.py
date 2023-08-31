import numpy as np

def hello():
    return "world"

def mean(df, column):

    return str(np.nanmean(df[column]))