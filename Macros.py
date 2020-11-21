"""
 @Time : 20/11/2020 13:08
 @Author : Alaa Grable
 """
# p0 = n0/(n0+n1)
calculate_p0 = lambda n0, n1: (n0 / (n0 + n1)) if (n0 + n1) != 0 else 0
# p1 = n1/(n0+n1)
calculate_p1 = lambda n0, n1: (n1 / (n0 + n1)) if (n0 + n1) != 0 else 0
# pMissing = nMissing/n, n=n0+n1+nMissing=number of individuals
calculate_p_missing = lambda n_missing, n: n_missing / n if n != 0 else 0
# segregation = (n0+n1)*((p0-0.5)^2)/0.5+(p1-0.5)^2)/0.5)
calculate_segregation = lambda n0, n1, p0, p1: ((n0 + n1) * ((p0 - 0.5) ** 2) / 0.5 + (p1 - 0.5) ** 2) / 0.5
# min((n01+n10), (n00+n11))/(n00+n01+n10+n11)
calculate_recombination_rate = lambda n00, n01, n10, n11: min((n01 + n10), (n00 + n11)) / (n00 + n01 + n10 + n11)
