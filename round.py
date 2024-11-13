def round_to_2(num):
   return round(num, 2)

# Příklady použití:
z1 = (-2 - (-1))/0.5302694733 
z2 = (-0.5 - (-1))/0.5302694733 



print(f"z1 rounded: {round_to_2(z1)}") 
print(f"z2 rounded: {round_to_2(z2)}") 

z3 = 0.67
sigma = 0.5302694733
mu = -1

y = mu + z3 * sigma
print(f"y rounded: {round_to_2(y)}") # -0.64