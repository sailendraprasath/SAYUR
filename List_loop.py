"""
List and Loop - Splitting and Summing Even and Odd Numbers
Description: Write a function sum_even_odd(lst) that takes a list of integers lst and returns a tuple with the sum of even numbers and the sum of odd numbers in the list.
sum_even_odd([1, 2, 3, 4, 5, 6])  # Output: (12, 9)
"""
numbers1 = [1, 2, 3, 4, 5, 6]

even_has = 0
odd_has = 0

for num in numbers1:
    if num % 2 == 0:
        even_has += num
    else:
        odd_has += num
print(f"even num is {even_has} and Odd num is {odd_has}")

"""sum_even_odd([10, 21, 32, 43, 54])  # Output: (96, 64)"""

given_value = [10, 21, 32, 43, 54]
even_has1 = 0
odd_has1 = 0

for num1 in given_value:
    if num1 % 2 == 0 :
        even_has1 += num1
    else:
        odd_has1 += num1
print(f"even num is {even_has1} and Odd num is {odd_has1}")