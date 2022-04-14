import sys
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


monibus = [
    [50, 8, 9000, 9],
    [70, 9, 3000, 10],
    [60, 5, 3000, 7],
    [90, 3, 3000, 6]
]
quadrada = numpy.square(monibus)
#print(quadrada)
#print("\n")

soma = numpy.sum(quadrada,0)
raiz = numpy.sqrt(soma)
#print (raiz)
#print("\n")

mn = monibus/raiz
#print (mn)

#print("\n")

alternatives = ["500", "504", "506", "540"]
criteria = ["tempo", "seguranca", "dist_andando", "conforto"]
weights = [0.3, 0.5, 0.05, 0.15]
cost_ben = ["c", "b", "c", "b"]

mnpesada = weights * mn
#print (mnpesada)

maxcoluna = mnpesada.max(axis=0)
#print (maxcoluna)
mincoluna = mnpesada.min(axis=0)
#print (mincoluna)

dif = mnpesada

print("\n")

for i in range (len(mnpesada)):
    for j in range (len(mnpesada[i])):
        if(cost_ben[j] == "b"):
            dif[i][j] = maxcoluna[j] - mnpesada[i][j]
        if(cost_ben[j] == "c"):
            dif[i][j] = abs(mincoluna[j] - mnpesada[i][j])
#print(dif)

#print ("\n")

somafinal = numpy.sum(dif,1)

print(somafinal)

sns.set_style("whitegrid")


a = sns.barplot( somafinal, palette="BuGn_d")
a.set_ylabel("Closeness Coefficient")
a.set_xlabel('Alternatives')
fig = a.get_figure()

plt.show()


########################################################################################################################
# Approach 1: using the csv file in "../test/dec_mat_2.csv"
########################################################################################################################
#print("-" * 50)
#print("- Approach 1:")
#print("-" * 50)
#tp = TOPSIS(monibus, cost_ben, weights=weights, alt_col_name="alternative", crit_col_names=criteria)
#tp.get_closeness_coefficient(verbose=True)
#tp.plot_ranking()
#print("-" * 50)
#print("")