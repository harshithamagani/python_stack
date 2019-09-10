#Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for x in nums:
            self.result = self.result + x
        self.result +=num
        return self
    def subtract(self, num, *nums):
        for x in nums:
            self.result = self.result - x
        self.result -=num
        return self

md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)    # should print 5
# run each of the methods a few more times and check the result!
