#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
#Michael
#John
#Mark
#KB

#And iterateDictionary2('last_name', students) should output:
#Jordan
#Rosales
#Guillen
#Tonel

def iterateDictionary(key_name='last_name', some_list=[]):
    for item in some_list:
        print(item[key_name])

#students[0]['last_name'] = 'Bryant'

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
            ]
iterateDictionary('first_name',students)





