# PROBLEMS ON LISTS

# Problem 1: Combine two lists index-wise(columns wise)

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

fruits = ['apple' , 'cherry', 'banana', 'grapes']
vegetables = ['eggplant', 'carrot', 'cucubumer', 'bottleguard']

result = []

for i,j in zip(fruits,vegetables):
    result.append([i,j])

print(result)