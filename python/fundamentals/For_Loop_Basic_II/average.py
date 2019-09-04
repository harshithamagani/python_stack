#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum=0
    for x in range(len(list)):
        sum+=list[x]
    return sum/len(list)


print(average([1,2,3,4]))

