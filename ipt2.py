from math import comb

def hypergeometric_calc(N, K, n, k):
    """
    N = celkový počet prvků
    K = počet prvků s danou vlastností
    n = velikost výběru
    k = počet úspěchů ve výběru
    """
    return comb(K, k) * comb(N-K, n-k) / comb(N, n)

# Parametry úlohy
N = 14  # celkový počet výrobků
K = 4   # počet vadných výrobků
n = 5   # velikost výběru

# Výpočet pravděpodobností
P_X_4 = hypergeometric_calc(N, K, n, 4)
P_X_less_4 = sum(hypergeometric_calc(N, K, n, k) for k in range(0, 4))
P_X_leq_4 = sum(hypergeometric_calc(N, K, n, k) for k in range(0, 5))
P_X_greater_4 = sum(hypergeometric_calc(N, K, n, k) for k in range(5, min(n+1, K+1)))
P_X_geq_4 = sum(hypergeometric_calc(N, K, n, k) for k in range(4, min(n+1, K+1)))
F_4 = P_X_leq_4

# Výpočet střední hodnoty a rozptylu
EX = n * K / N
DX = n * (K/N) * (1 - K/N) * (N-n)/(N-1)

print(f"P(X=4) = {P_X_4:.4f}")
print(f"P(X<4) = {P_X_less_4:.4f}")
print(f"P(X<=4) = {P_X_leq_4:.4f}")
print(f"P(X>4) = {P_X_greater_4:.4f}")
print(f"P(X>=4) = {P_X_geq_4:.4f}")
print(f"F(4) = {F_4:.4f}")
print(f"E(X) = {EX:.4f}")
print(f"D(X) = {DX:.4f}")