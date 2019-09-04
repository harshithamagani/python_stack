#Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def values_greater_than_second(list):
    newList = []
    if len(list) <= 2:
        return False
    secVal = list[1]
    for item in list:
        # TODO: write code...
        if item > secVal:
            newList.append(item)
    print(len(newList));
    return newList


print(values_greater_than_second([1,2,3,4,5]))



