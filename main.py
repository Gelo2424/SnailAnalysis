import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

data = pd.read_csv("data.csv", header=None)
index = ["Length", "Diameter", "Height", "WholeWeight", "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"]
indexp = ["Sex", "Length", "Diameter", "Height", "WholeWeight", "ShuckedWeight", "VisceraWeight", "ShellWeight",
          "Rings"]
# 3.1

countOfEachGender = data[0].value_counts()
percentageOfEachGender = data[0].value_counts(normalize=True) * 100
tableData = {'count': countOfEachGender.values.tolist(), '%': percentageOfEachGender.values.tolist()}
table1 = pd.DataFrame(tableData, index=["Male", "Infant", "Female"])
# print(table1)

# 3.2

table2 = data.describe().T.drop(['count'], axis=1)
table2.set_axis(index, axis=0, inplace=True)
# print(table2)

# 3.3

# plt.bar(["Male", "Infant", "Female"], countOfEachGender, width=0.35)
# plt.title("Liczebność poszczególnych płci")
# plt.show()

# 3.4

# fig, axes = plt.subplots(4, 2, figsize=(8, 7))
# axes = axes.ravel()
# for idx, ax in enumerate(axes):
#     ax.hist(data[:][idx + 1], 15, edgecolor="black")
#     ax.set_title(index[idx])
# plt.show()

# 4.2

# i = 1
# j = 2
# fig, axes = plt.subplots(14, 2, figsize=(7, 25))
# axes = axes.ravel()
# for idx, ax in enumerate(axes):
#     ax.scatter(data[:][i], data[:][j], s=5)
#     ax.set_xlabel(index[i-1])
#     ax.set_ylabel(index[j-1])
#     print(i, j)
#     if j == 8:
#         i += 1
#         j = i
#     if j < 8:
#         j += 1
#     else:
#         j = 1
# plt.show()

# 4.3

# tableCorrelation = data.drop([0], axis=1).corr()
# tableCorrelation.set_axis(index, axis=0, inplace=True)
# tableCorrelation.set_axis(index, axis=1, inplace=True)
# print(tableCorrelation.to_string())

# 4.4

# fig, ax = plt.subplots(figsize=(15, 5))
# sb.heatmap(tableCorrelation, cmap="Blues", linewidths=0.5)
# ax.xaxis.tick_top()
# plt.xticks(np.arange(8) + .5, labels=index)
# plt.show()

# 4.5

# specificData = data[[1, 2]]
# specificData.columns = ["Length", "Diameter"]
# sb.regplot(x="Length", y="Diameter", data=specificData,
#            scatter_kws={'s': 10, 'alpha': 0.5})
# plt.show()

# 5.2

data.columns = indexp
table4 = data.groupby('Sex').describe().stack().T.stack(0)
table4 = table4.rename_axis(["Feature", "Sex"], axis=0)
# print(table4)

# 5.3

table5 = data.groupby('Sex')
female = table5.get_group("F")
infant = table5.get_group("I")
male = table5.get_group("M")

fig, axes = plt.subplots(4, 2, figsize=(10, 20))
axes = axes.ravel()
for idx, ax in enumerate(axes):
    ax.boxplot([female.iloc[:, idx+1], infant.iloc[:, idx+1], male.iloc[:, idx+1]])
    ax.set_xticklabels(["Female", "Infant", "Male"])
    ax.set_title(index[idx])
plt.show()


