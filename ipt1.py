import random

def single_trial():
    a = random.uniform(0, 6)
    b = random.uniform(0, 6)
    return a + b <= 10.2

def simulation(num_trials):
    success_single = 0
    success_both = 0
    success_one = 0
    for _ in range(num_trials):
        trial1 = single_trial()
        if trial1:
            success_single += 1
        
        trial2 = single_trial()
        if trial1 and trial2:
            success_both += 1
        elif trial1 or trial2:
            success_one += 1
    
    return success_single / num_trials, success_both / num_trials, success_one / num_trials

num_trials = 1000000

prob_single, prob_both, prob_one = simulation(num_trials)

print(f"Vysledky simulacie (pocet pokusov: {num_trials}):")
print(f"1. Pravdepodobnost pre jeden pokus: {prob_single:.6f}")
print(f"2. Pravdepodobnost pre oba pokusy: {prob_both:.6f}")
print(f"3. Pravdepodobnost pre prave jeden z dvoch pokusov: {prob_one:.6f}")

# Teoretický výpočet
p = (10.2 / 6) ** 2 / 4  # pravdepodobnosť pre jeden pokus
theoretical_prob_single = p
theoretical_prob_both = p ** 2
theoretical_prob_one = 2 * p * (1 - p)

print("\nTeoreticke pravdepodobnosti:")
print(f"1. Pravdepodobnost pre jeden pokus: {theoretical_prob_single:.6f}")
print(f"2. Pravdepodobnost pre oba pokusy: {theoretical_prob_both:.6f}")
print(f"3. Pravdepodobnost pre prave jeden z dvoch pokusov: {theoretical_prob_one:.6f}")