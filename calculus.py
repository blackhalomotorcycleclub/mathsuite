import sympy

x = sympy.Symbol('x')

def limit(expression, x_value):
    result = sympy.limit(expression, x, x_value)
    return result

def derivative(expression):
    result = sympy.diff(expression, x)
    return result

def integral(expression):
    result = sympy.integrate(expression, x)
    return result

print('Welcome to our calculus lesson!')
print('In calculus, we study how things change. There are three main concepts in calculus: limits, derivatives, and integrals.')
print('A limit is the value that a function approaches as the input approaches some value.')
print('Let\'s see an example:')

expression = 1 / x
x_value = 0
result = limit(expression, x_value)
print(f'The limit of {expression} as x approaches {x_value} is {result}')

print('A derivative is a measure of how a function changes as its input changes.')
print('Let\'s see an example:')

expression = x ** 2
result = derivative(expression)
print(f'The derivative of {expression} is {result}')

print('An integral is the opposite of a derivative. It gives the area under the curve of a function.')
print('Let\'s see an example:')

expression = x ** 2
result = integral(expression)
print(f'The integral of {expression} is {result}')