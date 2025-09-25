'''Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

Original_list = list(range(1,11))
print(f"Original list: {Original_list}")
Extracted_list = Original_list[:5]
print(f"Extracted first five elements: {Extracted_list}")
Reversed_list = Extracted_list[::-1]
print(f"Reversed extracted elements: {Reversed_list}")