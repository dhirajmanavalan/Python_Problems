'''
Find the second largest number in a list

👉 Example:
Input: [10, 20, 4, 45, 99]
Output: 45
'''

numbers = [10, 20, 4, 45, 99]

unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print("Second largest number is:", second_largest)