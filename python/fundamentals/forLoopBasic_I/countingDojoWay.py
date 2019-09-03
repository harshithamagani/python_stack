#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(0,101):
    if(x%10==0):
        print("Coding Dojo",x)
    if(x%5==0):
        print("Coding",x)

