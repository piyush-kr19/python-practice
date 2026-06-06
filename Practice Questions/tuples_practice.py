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

# Q2: Multiply Adjacent elements (both side) and take sum of right and left side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)

test_tuple = (1, 5, 7, 8, 10)

result = []
for i in range(len(test_tuple)):
    if i == 0: # for first element
        value = test_tuple[i] * test_tuple[i+1]
        
    elif i == len(test_tuple) -1: # for last element
        value = test_tuple[i] * test_tuple[i-1]
    
    else: # for middle element
        value = test_tuple[i] * test_tuple[i-1] + test_tuple[i] * test_tuple[i+1]
        
    result.append(value)
    
print(tuple(result))

# Q3: Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same

t1 = (1,2,3,0)
t2 = (0,1,2,3)

if t1 == t2:
    print("Same")
else:
    print("Different")
    
# Both tuples have similar values but still it is different becuse tuples are stored in ordered way

# Q4: Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

l = 0
s = 0
t = 0

for item in list1:
    if type(item) == list:
        l += 1
    elif type(item) == set:
        s += 1
    elif type(item) == tuple:
        t += 1

print('List-',l)
print('Set-',s)
print('Tuple-',t)


# Q5: Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# Show every students record in form of tuples if matches all required criteria.

# It is assumed that there will be only one primry skill.

# If no such candidate found, print No such candidate

# Input:

# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
# Output

# ('Manohar', 'B.tech', 'Python', '2022')

n = int(input("Enter no. of records: "))

students = []
for i in range(1,n+1):
    print("Enter Details of student-",i)

    Name = input("Enter Student name: ")
    Study = input("Enter Higher Education: ")
    Skill = input("Enter Primary Skill: ")
    Year = input("Enter Year of Graduation: ")

    students.append((Name,Study,Skill,Year))

print("\nEnter Job Role Requirement")
req_education = input("Enter Higher Education: ")
req_skill = input("Enter Skill: ")
req_graduation = input("Enter Year of Graduation: ")


found = False

for student in students:
    if (student[1] == req_education and
        student[2] == req_skill and
        student[3] == req_graduation):
        print(student)
        found = True

if not found:
    print("No such Candidate")

# ------TUPLES COMPLETED------