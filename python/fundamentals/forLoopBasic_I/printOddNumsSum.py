
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum=0
for x in range(1,51,2):
    print(x,sum)
    sum+=x
print(sum)
