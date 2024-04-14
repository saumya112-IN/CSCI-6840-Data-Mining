import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import random
directory = os.fsencode("./ca-pv-2006")
fileData = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv") and filename.startswith("Actual"):
        data = filename.replace('_', ' ').replace(', ', ' ').split()
        openfile = open("./ca-pv-2006/"+filename)
        csvreader = csv.reader(openfile)
        rowslice = slice(0,8)
        powerOnDate = 0
        for row in csvreader:
            if row[1] != "Power(MW)":
                powerOnDate += float(row[1])
        openfile.close()
        data.append(powerOnDate)
        fileData.append(data)

    else:
        continue
mapData = []
for row in fileData:
    data = []
    lat = float(row[1])+(random.random()-.5)
    long = float(row[2])+(random.random()-.5)
    data.append(lat)
    data.append(long)
    mw = float(row[5][:-2])
    avg = row[8]/mw
    data.append(avg)
    mapData.append(data)

df=pd.DataFrame(mapData,columns=["latitude","longitude","Adjusted Power Generated"])

df.plot.scatter(x='longitude', y='latitude', c='Adjusted Power Generated',
                colormap='plasma',
                title="Actual Solar Power Map in 2006")
plt.show()