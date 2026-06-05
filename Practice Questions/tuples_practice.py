# PROBLEMS ON TUPLES

# Q1: Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

# For eg.

# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

d = {}

for a, b in test_list:
    if a not in d:
        d[a] = [a]
    d[a].append(b)

result = []
for values in d.values():
    result.append(tuple(values))

print(result)

# Q2: Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)
