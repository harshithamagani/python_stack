#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0 :
            list[x]="big"
    return list


print(biggie_size([2,5,-3,5,-1,4,-2]))

