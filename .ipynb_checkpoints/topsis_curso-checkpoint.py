import sys
#sys.path.append("../src")
#from decision_making import TOPSIS
from topsis import TOPSIS

#dec_mat_2 = [
#    [15, 6, 25000, 7],
#    [12, 7, 35000, 7],
#    [10, 9, 55000, 8]
#]
monibus = [
    [50, 8, 9000, 9],
    [70, 9, 3000, 10],
    [60, 5, 3000, 7],
    [90, 3, 3000, 6]
]
alternatives = ["500", "504", "506", "540"]
criteria = ["tempo", "seguranca", "dist_andando", "conforto"]
#weights = [0.3, 0.5, 0.05, 0.15]
weights = [0.3, 0.5, 0.05, 0.15]

cost_ben = ["c", "b", "c", "b"]

########################################################################################################################
# Approach 1: using the csv file in "../test/dec_mat_2.csv"
########################################################################################################################
print("-" * 50)
print("- Approach 1:")
print("-" * 50)
tp = TOPSIS("../cursoml/topsis/matriz_onibus.csv", cost_ben, weights=weights, alt_col_name="alternative", crit_col_names=criteria)
tp.get_closeness_coefficient(verbose=True)
tp.plot_ranking()
print("-" * 50)
print("")