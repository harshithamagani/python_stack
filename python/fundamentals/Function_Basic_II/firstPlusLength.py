#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    return list[0]+len(list)

print(first_plus_length([1,2,3,4,5]))



