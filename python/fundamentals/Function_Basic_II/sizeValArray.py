#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    
    return newList


print(length_and_value(4,7))
print(length_and_value(6,2))


