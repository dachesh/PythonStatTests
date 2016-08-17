# regression model
import numpy as np
import scipy as sp
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns

dublin = pd.read_csv('/Users/eshelman/documents/Dulles_Data2.csv', sep=',')
dublin['TMAXF'] = (dublin['TMAX']*.18)+32
dublin['TMINF'] = (dublin['TMIN']*0.18)+32
print(dublin.head())

regres = sp.stats.linregress(dublin['TMIN'], dublin['TMAXF'])
print(regres)


#print(sns.lmplot('DATE','TMAXF',dublin))
#plt.show(block=False)