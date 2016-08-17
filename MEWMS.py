#MEWMS.py

import csv
import numpy as np
import scipy as sp
import pandas as pd

filenm = '/Users/eshelman/code/Python/DCGS_BMS_Trends/PDX4Pod20_Humidity.csv'
humdat = pd.read_csv(filenm, header=0, sep=',')
humdat = humdat[pd.notnull(humdat)]


meanvec = np.array(humdat.mean(axis=0))
devivec = np.array(np.std(humdat, axis=0))

#print(humdat.head(n=5))

omega = 0.5
L = 1624
S = 0

vecdat = humdat.drop('DateTime', 1)
vecdat = pd.DataFrame.as_matrix(vecdat)

#print(vecdat.head(n=5))
for row in vecdat:
	#print(row)
	arr = np.array(row, dtype=np.float64)
	if np.isnan(np.min(arr)):
		continue

	vect = np.subtract(arr, meanvec)
	print(vect)
	#print(meanvec)

	standard = np.true_divide(vect,devivec)
	S = np.add(np.multiply(omega, np.sqrt(np.dot(standard, standard))), np.multiply((1-omega), S))

print(S)