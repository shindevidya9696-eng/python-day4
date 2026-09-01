# 1.
# numbers = (10, 20, 30, 40, 50)

# print(numbers)

# 2.
# numbers = (10, 20, 30, 40, 50)

# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# 3.
# numbers = (10, 20, 30, 40, 50)

# print("Length:", len(numbers))

# 4.
# numbers = (10, 20, 30, 20, 40, 20)

# print("Count of 20:", numbers.count(20))

# 5.
# numbers = (10, 20, 30, 40, 50)

# # print("Index of 30:", numbers.index(30))
# 6.
# student = ("Vidya", 22, "Computer Science")

# name, age, course = student

# print("Name:", name)
# print("Age:", age)
# print("Course:", course)


# 7.
# student = ("Vidya", 22, "Computer Science", 70, "Pune")

# print(student)

# 8.
# numbers = {10, 20, 30, 40, 50}

# print(numbers)

# 9.
# numbers = {10, 20, 30, 40, 50}

# numbers.add(60)

# # print(numbers)
# 10.
# numbers = {10, 20, 30, 40, 50}

# numbers.remove(30)

# print(numbers)

# 11.
# numbers = [10, 20, 20, 30, 30, 40, 50, 50]

# unique_numbers = set(numbers)

# print(unique_numbers)

# 12.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}

# result = set1.union(set2)

# print(result)

# 13.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}

# result = set1.intersection(set2)

# print(result)


# 14.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}

# result = set1.difference(set2)

# print(result)

# 15.
# student = {
#     "name": "Vidya",
#     "age": 22,
#     "course": "Computer Science"
# }

# print(student)


# 16.
# student = {
#     "name": "Vidya",
#     "age": 22,
#     "course": "Computer Science"
# }

# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Course:", student["course"])
# 17.
# student = {
#     "name": "Vidya",
#     "age": 22
# }

# student["city"] = "Pune"

# print(student)

# 18.
# student = {
#     "name": "Vidya",
#     "age": 22
# }

# student["age"] = 23

# print(student)

# 
# 19.
# student = {
#     "name": "Vidya",
#     "age": 22,
#     "city": "Pune"
# }

# del student["city"]

# print(student)

# 20.
# student = {
#     "name": "Vidya",
#     "age": 22,
#     "city": "Pune"
# }

# print("Keys:", student.keys())
# print("Values:", student.values())
# print("Items:", student.items())

# 21.
# student = {
#     "name": "Vidya",
#     "age": 22,
#     "city": "Pune"
# }

# if "name" in student:
#     print("Key exists")
# else:
#     print("Key does not exist")

# 22.
# marks = {
#     "Vidya": 85,
#     "Aakansha": 78,
#     "Omkar": 92,
#     "Viraj": 68
# }

# print(marks)

# 23.
# students = [
#     {"name": "Vidya", "marks": 85},
#     {"name": "Om", "marks": 78},
#     {"name": "Deva", "marks": 92},
#     {"name": "Sam", "marks": 68},
#     {"name": "Rahul", "marks": 74}
# ]

# print(students)

24.
students = [
    {"name": "Vidya", "marks": 85},
    {"name": "Om", "marks": 78},
    {"name": "Deva", "marks": 92},
    {"name": "Viraj", "marks": 68},
    {"name": "Rahul", "marks": 74}
]

for student in students:
    if student["marks"] > 75:
        print(student["name"], student["marks"])