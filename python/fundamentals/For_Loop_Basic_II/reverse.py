#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def reverse_list(list):
    for x in range (0,len(list)//2):
        temp = list[x]
        list[x] = list[len(list)-1-x]
        list[len(list)-1-x] = temp
    return list


print(reverse_list([37,2,1,-9]))
