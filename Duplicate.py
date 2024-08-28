"""" Problem 3: Looping Through Lists - Removing Duplicates
Description: Write a function remove_duplicates(lst) that takes a list lst and returns a new list with duplicates removed, preserving the original order.
remove_duplicates([1, 2, 2, 3, 4, 4, 5])   Output: [1, 2, 3, 4, 5] """

# val1 = [1,2,2,3,4,4,5]
# val2 = []

# for val3 in val1:
#     if val3 not in val2:
#         val2.append(val3)

# print(val2)

"""remove_duplicates(["apple", "banana", "apple", "orange"])  # Output: ["apple", "banana", "orange"] """

Fruits = ["apple", "banana", "apple", "orange"]
Final_list =[]

for fruit1 in Fruits:
    if fruit1 not in Final_list:
        Final_list.append(fruit1)

print(Final_list) 
  