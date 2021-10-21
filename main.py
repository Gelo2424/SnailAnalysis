import pandas as pd

data = pd.read_csv("data.csv", header=None)

maleNum = (data[:][0] == 'M').sum()
femaleNum = (data[:][0] == 'F').sum()
infantNum = (data[:][0] == 'I').sum()

print((data[:][0] == 'I').sum())
