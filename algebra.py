from sympy import Eq, solve

x = sympy.Symbol('x')

def solve_equation(equation):
    result = solve(equation)
    return result

def simplify_expression(expression):
    result = sympy.simplify(expression)
    return result

print('Welcome to our algebra lesson!')
print('In algebra, we use letters to represent numbers and study how to manipulate them.')
print('One of the main concepts in algebra is solving equations.')
print('Let\'s see an example:')

equation = Eq(x ** 2 - 1, 0)
result = solve_equation(equation)
print(f'The solutions to the equation {equation} are {result}')

print('Another important concept in algebra is simplifying expressions.')
print('Let\'s see an example:')

expression = (x ** 2 - 1) / (x + 1)
result = simplify_expression(expression)
print(f'The simplified form of the expression {expression} is {result}')