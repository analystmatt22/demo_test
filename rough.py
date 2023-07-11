import pandas as pd
import numpy as np


data = pd.read_excel('./CovidDeaths.xlsx')
print(data.__len__)

def new_func(data):
    print(data.keys())

new_func(data)