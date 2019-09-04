#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def maximum(list):
    max=0
    if len(list) == 0 :
        return False
    for x in list:
        if x > max:
            max=x
    return max


print(maximum([37,2,1,-9]))
print(maximum([]))
