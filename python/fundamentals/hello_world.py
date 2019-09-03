
print("Hello World!")


x = "Hello Python"
print(x)
y = 42
print(y)

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

#F-Strings (Literal String Interpolation)
first_name="Zen"
last_name="Coder"
age=27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#string.format()
print("My name is {} {} and I am {} year old.".format(first_name,last_name,age))

print ("My name is {} {} and I am {} years old.".format(age,first_name,last_name))

#%-formatting

hw = "Hello %s" % "world"     # with literal values
py = "I love Python %d" % 3
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))        # or with variables
# output: My name is Zen and I'm 27

x = "hello world"
print(x.title())
