print("Hello World")

name="Harshitha"

print("Hello",name,"!")
print("Hello "+name+" !")

num=8

print("Hello",num,"!")
print("Hello"+str(num)+"!")
print(f"Hello {num} !")
print("Hello {} !".format(num))
print("Hello %d !"%(num))

food1="fried rice"
food2="gravy"

print("I love to eat {} and {}".format(food1,food2))
print(f"I love to eat {food1} and {food2}")

print(food1.upper())
print(food1.lower())
print(food1.count("ice"))
print(food1.split(" "))

x=10

if x>50:
    print("bigger then 50")
else:
    print("smaller then 50")

#Tuples
dog = ("Bruce","cocker spaniel",19, False) #Tuples are immutable
print(dog[0])		# output: Bruce
#dog[1] = 'dachshund' error since 

#Lists

empty_list=[]
ninjas=['Rozen','KB','Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

#Dictionaries

empty_dict = {}
new_person = {'name':'John','age':38,'weight':160.2,'has_glasses':False}
new_person['name']='Jack'
new_person['hobbies'] = ['climbing','coding']
print(new_person)
w = new_person.pop('weight')
print(w)
print(new_person)

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

#print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

#For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:

print(len(new_person))        # output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))    # output: 11

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        continue
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1
