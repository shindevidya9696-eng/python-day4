# 1.
# numbers = []

# numbers.append(10)
# numbers.append(15)

# numbers.extend([20, 30])
# numbers.extend([40, 50])

# print(numbers)

# 2.
# items = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# items.remove("C++")

# last_item = items.pop()

# print("Modified list:", items)
# print("Last item:", last_item)


# 3.
# scores = [85, 92, 75, 92, 88, 92, 70]

# count_92 = scores.count(92)
# index_88 = scores.index(88)

# print("Count of 92:", count_92)
# print("Index of 88:", index_88)

# 4.
# marks = [67, 12, 89, 45, 95, 34]

# marks.sort()
# print("Ascending:", marks)

# marks.reverse()
# print("Descending:", marks)

# 5.
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 1. First 5 elements
# print("First 5 elements:", arr[:5])

# # 2. Last 3 elements
# print("Last 3 elements:", arr[-3:])

# # 3. Every second element from index 1 to index 8
# print("Every second element:", arr[1:9:2])

# # 4. List in reverse order
# print("Reverse order:", arr[::-1])

# 6.
# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# total = 0

# for num in numbers:
#     total = total + num

# average = total / 5

# print("List:", numbers)
# print("Sum:", total)
# print("Average:", average)

# 7.
# def find_min_max(numbers):
#     maximum = numbers[0]
#     minimum = numbers[0]

#     for num in numbers:
#         if num > maximum:
#             maximum = num

#         if num < minimum:
#             minimum = num

#     return maximum, minimum


# numbers = [34, 12, 89, 5, 67]

# maximum, minimum = find_min_max(numbers)

# print("Max =", maximum)
# print("Min =", minimum)

# 8.
# numbers = [1, 3, 2, 3, 4, 1, 5, 2]

# unique_numbers = []

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# print("Original list:", numbers)
# print("List without duplicates:", unique_numbers)

# 9.
# numbers = [10, 15, 22, 33, 40, 55, 60]

# even_list = []
# odd_list = []

# for num in numbers:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("Even:", even_list)
# print("Odd:", odd_list)

# 10.
# numbers = [10, 45, 20, 99, 80, 99]

# largest = float('-inf')
# second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second Largest:", second_largest)
# 11.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squares = [num ** 2 for num in nums if num % 2 != 0]

# print(squares)
# 12.
# def rotate_left(lst, k):
#     k = k % len(lst)
#     return lst[k:] + lst[:k]


# lst = [1, 2, 3, 4, 5]
# k = 2

# result = rotate_left(lst, k)

# print("Rotated list:", result)

# 13.
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8, 10]

# merged = []
# i = 0
# j = 0

# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         merged.append(list1[i])
#         i += 1
#     else:
#         merged.append(list2[j])
#         j += 1

# while i < len(list1):
#     merged.append(list1[i])
#     i += 1

# while j < len(list2):
#     merged.append(list2[j])
#     j += 1

# print("Merged List:", merged)

# 14.
# def flatten(nested_list):
#     result = []

#     for item in nested_list:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)

#     return result


# nested_list = [1, [2, 3], [4, [5, 6]], 7]

# print("Input:", nested_list)
# print("Output:", flatten(nested_list))
# 15.
# def find_pairs(nums, target):
#     pairs = []

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 pairs.append((nums[i], nums[j]))

#     return pairs


# nums = [2, 4, 3, 5, 7, 8, 9]
# target = 7

# result = find_pairs(nums, target)

# print("Pairs:", result)

# 16.
# def longest_consecutive(nums):
#     num_set = set(nums)
#     longest = 0

#     for num in num_set:
#         # Check if num is the starting number
#         if num - 1 not in num_set:
#             current = num
#             length = 1

#             # Find consecutive numbers
#             while current + 1 in num_set:
#                 current += 1
#                 length += 1

#             longest = max(longest, length)

# #     return longest


# # # Input
# # nums = [100, 4, 200, 1, 3, 2]

# # # Output
# # print("Length:", longest_consecutive(nums))
# 17.
# def group_anagrams(words):
#     anagrams = {}

#     for word in words:
#         key = ''.join(sorted(word))

#         if key not in anagrams:
#             anagrams[key] = []

#         anagrams[key].append(word)

#     return list(anagrams.values())


# # Input
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# # Output
# print(group_anagrams(words))

# 18.
# a = [1, 2, [3, 4]]
# b = a.copy()

# b[0] = 99
# b[2][0] = 77

# print("a:", a)
# print("b:", b)

19.







