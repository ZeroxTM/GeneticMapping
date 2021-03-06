"""
 @Time : 20/11/2020 13:08
 @Author : Alaa Grable
 """
import numpy as np

# p0 = n0/(n0+n1)
calculate_p0 = lambda n0, n1: round(n0 / (n0 + n1), 2) if (n0 + n1) != 0 else 0
# p1 = n1/(n0+n1) # Allele frequency
calculate_p1 = lambda n0, n1: round(n1 / (n0 + n1), 2) if (n0 + n1) != 0 else 0
# pMissing = nMissing/n, n=n0+n1+nMissing=number of individuals
calculate_p_missing = lambda n_missing, n: round(n_missing / n, 2) if n != 0 else 0
# segregation = (n0+n1)*((p0-0.5)^2)/0.5+(p1-0.5)^2)/0.5)
calculate_segregation = lambda n0, n1, p0, p1: round(((n0 + n1) * ((p0 - 0.5) ** 2) / 0.5 + (p1 - 0.5) ** 2) / 0.5, 2)
# min((n01+n10), (n00+n11))/(n00+n01+n10+n11)
calculate_recombination_rate = lambda n00, n01, n10, n11: round(min((n01 + n10), (n00 + n11)) / (n00 + n01 + n10 + n11),
                                                                4) \
    if (n00 + n01 + n10 + n11 != 0) else 0


def calculate_kossambi_distance(r):
    if r >= 0.5:
        r = 0.49
    return round((1 / 4) * np.log((1 + 2 * r) / (1 - 2 * r)) * 100, 2)


def calculate_haldane_distance(r):
    if r >= 0.5:
        r = 0.49
    return round(-50 * np.log(1 - 2 * r), 2)
