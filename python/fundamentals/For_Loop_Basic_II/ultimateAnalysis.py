#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    dict={}
    sumTotal=0
    average=0
    minimum=0
    maximum=0
    length=len(list)
    if len(list) == 0 :
        return False
    for x in list:
        if x > maximum:
            maximum=x
        elif x < minimum:
            minimum = x
        sumTotal+= x
    average =  sumTotal/length
    dict['sumTotal']=sumTotal
    dict['average']=average
    dict['minimum']=minimum
    dict['maximum']=maximum
    dict['length']=length
    return dict


print(ultimate_analysis([37,2,1,-9]))
print(ultimate_analysis([]))
