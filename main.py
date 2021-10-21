import pandas as pd

data = pd.read_csv("data.csv", header=None)

countOfEachGender = data[0].value_counts()
percentageOfEachGender = data[0].value_counts(normalize=True) * 100
tableData = {'count': countOfEachGender.values.tolist(), '%': percentageOfEachGender.values.tolist()}
df = pd.DataFrame(tableData, index=["Male", "Infant", "Female"])

columns=['mean', 'std', 'min', '25%', '50%', '75%', 'max']
index=["Length", "Diameter", "Height", "WholeWeight", "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"]

tableData2 = data.describe().T.drop(['count'], axis=1)

print(tableData2)
print(pd.DataFrame(tableData2, index=index))

