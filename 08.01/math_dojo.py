class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
md = MathDojo()

x = md.add(10).add(15, 20).add(15, 20, 25).result
print(x) 

y = md.subtract(5).subtract(5, 10).subtract(5, 10, 15).result
print(y) 