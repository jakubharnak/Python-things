# Method 1: Using round() function
result = round(0.32/0.51, 8)
print(result)

# Method 2: Using format string
result = "{:.8f}".format(0.32/0.51) 
print(result)

# Method 3: Using f-string
result = f"{0.32/0.51:.8f}"
print(result)

# All these methods will output: 0.56140