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
    
    
# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,3,6,10,15,21]

list1 = [1,2,3,4,5,6]

sum = 0
result = []

for i in list1:
    sum += i
    result.append(sum)
print(result)


# Problem 5: You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
# i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

# For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

# For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

# like wise for all other elememts.

# [2,4,6,10,1]-->[22,20,16,10,23]


list1 = [2,4,6,10,1]

resultant = []
for i in (list1):
    total = 0
    for j in list1:
        if j >= i:
            total += j
        resultant.append(total)

print(resultant)

# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:

# [34, 67, 89]

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

result = []

for i in num1:
    if i in num2:
        result.append(i)

result.sort()
print(result)

# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:

# ['1ac21', '23fg', '456', '098d','1','kls']
# Output:

# ['456', '23fg', '1ac21', '1', 'kls', '098d']

l1 = ['1ac21', '23fg', '456', '098d','1','kls']

result = []

for s in l1:
    product = 1

    for i in s:
        if i.isdigit():
            product *= int(i)

    result.append((product,s))

result.sort(reverse = True)

sorted_list = []

for product, s in result:
    sorted_list.append(s)

print(sorted_list)

# Problem 8: Split String of list on K character.

# Example :

# Input:

# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:

# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

C = ['CampusX is a channel', 'for data-science', 'aspirants.']

result = []

for i in C:
    words = (i.split())
    result.extend(words)

print(result)

# Problem 9: Convert Character Matrix to single String using string comprehension.
# Example 1:

# Input:

# [['c', 'a', 'm', 'p', 'u', 's', 'X'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
# Output:

# campusX is best channel

C1 = [['c', 'a', 'm', 'p', 'u', 's', 'X'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
words = []

for i in C1:
    words.append(((''.join(i))))

# print(words)

result = ' '.join(words)

print(result)

# Problem 11: Write a program that can perform union operation on 2 lists
# Example:

# Input:

# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:

# [1,2,3,4,5,7,8]

# METHOD 1
list1 = [1,2,3,4,5,1]
list2 = [2,3,5,7,8]
list3 = list1 + list2
result = []
for i in list3:
    if i not in result:
        result.append(i)
print(result)

# METHOD 2
l1 = [1,2,3,4,5,1]
l2 = [2,3,5,7,8]

result = list(set(l1) | set(l2))

print(result)

# Problem 12: Write a program that can find the max number of each row of a matrix
# Example:

# Input:

# [[1,2,3],[4,5,6],[7,8,9]]
# Output:

# [3,6,9]

l1 = [[1,2,3],[4,5,6],[7,8,9]]

result = []
for i in l1:
    result.append(max(i))

print(result)

# Problem 13: Write a list comprehension to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

for row in range(3):
    temp = []

    for column in range(3):
        temp.append(row*3 + column)

    print(temp)

result = [[row*3 + column for column in range(3)] for row in range(3)]

print(result)

# Problem 14: Write a list comprehension that can transpose a given matrix
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

# result = []
# for i in range(3):
#   transpose = []
#   for j in range(3):
#     transpose.append(matrix[j][i])
#   result.append(transpose)
# for row in result:
#     print(row)

result = [[matrix[j][i] for j in range(3)] for i in range(3)]
for row in result:
    print(row)

# Problem 15: Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

result = []
for i in range(3):
    for j in range(3):
        result.append(matrix[i][j])
print(result)

# COMPLETED THE PROBLEMS ON LISTS