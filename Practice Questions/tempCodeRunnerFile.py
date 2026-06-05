test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

for i in test_list:
    for j in test_list:
        if i[0] == j[0] and i != j:
            i += j[1:]
print(test_list)