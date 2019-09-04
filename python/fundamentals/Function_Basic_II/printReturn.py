
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list):
    for x in range(0,len(list)):
        if x == 0 :
            print(list[x])
        else:
            return list[x]

print(print_and_return([1,2]))




