import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns

testdat = pd.read_csv('/Users/eshelman/Documents/602 Assn 1.4.txt', sep='\t', header=None)
testdat.columns = ['diastolic', 'systolic', 'trt']

syst1 = testdat['systolic'][testdat['trt']==1]
syst2 = testdat['systolic'][testdat['trt']==2]
#print(syst1)

#out = sp.stats.ttest_rel(syst1, syst2)
out2 = sp.stats.ttest_ind(syst1, syst2)

#print(out)
print(out2)
#print(testdat.head())