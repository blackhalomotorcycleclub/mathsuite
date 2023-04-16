import os

def run_script(script_name):
    os.system(f'python {script_name}')

print('Welcome to the Math Learning Suite!')
print('Please select one of the following options:')
print('1. Calculus')
print('2. Algebra')
print('3. Trigonometry')
print('4. BEDMAS')

choice = input('Enter your choice: ')

if choice == '1':
    run_script('calculus.py')
elif choice == '2':
    run_script('algebra.py')
elif choice == '3':
    run_script('trigonometry.py')
elif choice == '4':
    run_script('bedmas.py')
else:
    print('Invalid choice.')