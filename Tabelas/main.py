import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv('titanic.csv')

table.plot(kind='bar')