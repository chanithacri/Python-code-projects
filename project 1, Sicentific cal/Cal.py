import math
# If you know how to use a Class
class Cal:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def mod(self):
        return self.num1 % self.num2
    def power(self):
        return self.num1 ** self.num2
    def root(self):
        return math.sqrt(self.num1)
    def log(self):
        return math.log(self.num1)
    def sin(self):
        return math.sin(self.num1)
    def cos(self):
        return math.cos(self.num1)
    def tan(self):
        return math.tan(self.num1)

# If you don't know how to use a Class
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def power(a, b):
    return a ** b
def root(a):
    return math.sqrt(a)
def log(a):
    return math.log(a)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)


# User input and function calling(You have to compleate this part)
# Star like this
if __name__ == "__main__":
    while True:
        print("Enter the operation you want to perform(+, -, /, *, %, **, squer root, cos, sin, tan, log) exit() to exit: ")
        oparation = input()
        if oparation == "exit()":
            print("Hope to see you again. Bye for now!")
            break
        else:
            pass
        print("Enter two numbers (for cos, sin, tan, log enter only one, sencond one no counted): ")
        # must add metord to check thet number inputs are valid numbers.
        x = int(input("num_1"))
        y = int(input("num_2"))
        ...
