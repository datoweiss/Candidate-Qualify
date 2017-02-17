import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Hello = np.array([])
Destination = '/Users/davidweiss/Desktop/Job.txt'
with open(Destination, 'r') as f:
    ar = pd.read_csv(f , delimiter='•',header = None)
x = pd.DataFrame([0]*len(ar))    
for row in ar.itertuples():  
    print (row[1])     
    try:
        Hello = np.append(Hello, int(input('\n Candidate Score? \n')))
    except ValueError:
            Hello = np.append(Hello, 'NaN')      
for row in Hello:
    try:
        if row > 10:
            Hello = np.append(Hello, 'NaN')
    except TypeError:
        if row == 'NaN':
            print('Gotta use numbers Dawg')

ad = pd.DataFrame(Hello)
ad.columns = ['David']
plt.figure()
ad=ad.astype(float)
ad.plot.box(vert=False, showmeans = True)
plt.xlabel('Candidate Score')
plt.ylabel('Candidate')
plt.show()
