# In the following exercise you will finish writing smallest_positive which is a function that finds the smallest positive number in a list.

def smallest_positive(in_list):
    x = None
    
    for item in in_list:
        if item <= 0:
            continue
        
        if x == None or item < x:
            x = item
            
    return x

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None