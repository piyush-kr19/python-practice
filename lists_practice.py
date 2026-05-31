# PROBLEMS ON LISTS

# Problem 1: Combine two lists index-wise(columns wise)

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

fruits = ['apple' , 'cherry', 'banana', 'grapes']
vegetables = ['eggplant', 'carrot', 'cucubumer', 'bottleguard']

result = []

for i,j in zip(fruits,vegetables):
    result.append([i,j])

print(result)

# Problem 2: Add new item to list after a specified item

# Write a program to add item 7000 after 6000 in the following Python List


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

print(list1[2][2].append(7000))

print(list1)

# Problem 3: Update no of items available
# Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

# i.e -

# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]
# Write a program to show no. of items of each candy type.

# Output:

# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

for i , j in zip(candy_list,no_of_items):
    print(f"{i}-{j}")