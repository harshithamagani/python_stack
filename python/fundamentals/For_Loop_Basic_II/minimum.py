#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(list):
    min=0
    if len(list) == 0 :
        return False
    for x in list:
        if x < min:
            min=x
    return min


print(minimum([37,2,1,-9]))
print(minimum([]))
