#Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def count_positives(list):
    count = 0
    for x in range(len(list)):
        if list[x] > 0 :
            count+=1
    print(count)
    list[len(list)-1]=count
    return list


print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

