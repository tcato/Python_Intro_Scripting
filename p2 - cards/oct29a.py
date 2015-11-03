__author__ = 'tcato'


def add(arg1, arg2):
    return arg1 + arg2

num1 = 3
num2 = 4
# Note the function is called within a "print" statement
# Note the parameters are passed to the arguments based on keyword argument
print('Twice the sum is', add(arg1=num1, arg2=num2) * 2)
