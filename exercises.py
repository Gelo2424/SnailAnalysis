import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 3, 7, 8])
b = np.array([[1, 7, 9], [2, 5, 8]])
c = np.array([1, 9, 3, 7, 5, 5, 8, 2]).reshape(2, 4)
d = np.arange(1, 10).reshape(3, 3)

e = b.T
f = a.T
g = a.reshape(1, 4).T
h = np.arange(1, 16).reshape(3, 5).T
i = np.array([1.0, 2.0, 4.0, 7.0])
j = np.array([5, 4, 2, 1]).astype("float64")
k = np.arange(0, 5)
l = np.arange(0, 5).astype("float64")
b.sum(axis=0)
b.sum(axis=1)

m = h[0:-1, 1:]
n = h[[1, 3],]

o = a
o[0] = -5

p = b[0]
p[0] = -3

r = c.copy()
r[0][0] = -2

s = d.T
s[0][1] = -1

t = np.array([8, 5, 7])
u = t[:, np.newaxis]
v = t * 5
w = np.array([2, 4, 3, 7])
x = c / w
y = np.array([2, 5])
z = c[np.newaxis, :]

temp = c < 5
temp = temp.astype("int32") * 3
c += temp

data = np.loadtxt("data.txt")
years = data[:, 0].astype(int)
popul_mean = data[:, 1:].mean(0)
popul_std = data[:, 1:].std(0)

data[:, 1:].max(0)
data[np.argmax(data, 0)[1]][0].astype(int)

species = np.array(["zające", "rysie", "marchewki"])
best_spiecies_for_year = species[np.argmax(data[:, 1:], 1)]
result = np.column_stack((data[:, 0].astype("int"), best_spiecies_for_year))

temp1 = np.any(data[:, 1:3] > 50000, 1)
temp2 = data[:, 0]
res = temp1 * temp2
res = res[res != 0]

# ######### MATPLOTLIB ########## #
# plt.title("LICZEBNOŚCI GATUNKÓW")
# plt.xlabel("Rok")
# plt.ylabel("Liczebność")
# plt.plot(years, data[:, 1], label="Zajace")
# plt.plot(years, data[:, 2], label="Rysie")
# plt.plot(years, data[:, 3], label="Marchew")
# plt.legend()
# plt.show()
#
# plt.title("Srednia liczebnosc")
# osx = ["Zajace", "Rysie", "Marchew"]
# plt.bar(osx, popul_mean, yerr=popul_std, capsize=10)
# plt.show()
#
# plt.boxplot(data[:, 1:])
# plt.xticks([1, 2, 3], osx)
# plt.show()

# plt.hist(data[:, 1], edgecolor="black")
# plt.show()


# fig, axs = plt.subplots(1, 3, figsize=(9.6, 4.8))
# axs[0].hist(data[:, 1], 5)
# axs[0].set_title("Zające")
# axs[1].hist(data[:, 2], 5)
# axs[1].set_title("Rysie")
# axs[2].hist(data[:, 3], 5)
# axs[2].set_title("Marchwie")
# plt.tight_layout()
# plt.show()
