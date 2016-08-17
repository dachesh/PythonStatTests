import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns

testdat = pd.read_csv('/Users/eshelman/Documents/602 Assn 1.4.txt', sep='\t', header=None)
testdat.columns = ['diastolic', 'systolic', 'trt']


anova = sp.stats.f_oneway(testdat['systolic'],testdat['diastolic'])

print(anova)
