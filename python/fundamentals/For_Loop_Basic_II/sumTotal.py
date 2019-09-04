
#Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
def sum_total(list):
    sum=0
    for x in range(len(list)):
        sum+=list[x]
    return sum


print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

