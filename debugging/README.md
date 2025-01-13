# ChatGPT - Introduction

## Description
Use ChatGPT to identify and correct errors in code samples.

## TASKS

### 0. Debugging - Python Factorial

#### Objectives
- Fix the code, it should print the factorial of the argument.
- Code to fix :

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

#### Expected result
➜  debugging git:(main) ✗ ./factorial.py 5
Le factoriel de 5 est 120.


### 1. Debugging - Python Arguments

#### Objectives
- Fix the code, it should print only the arguments without the python file name.
- Code to fix :

#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])

#### Expected result
➜  debugging git:(main) ✗ ./print_arguments.py 5
Liste des arguments passés au script :
Argument 0 : ./print_arguments.py
Argument 1 : 5
