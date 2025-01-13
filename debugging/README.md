# ChatGPT - Introduction

## TASKS

### 0. Debugging - Python Factorial

#### Objectives
- Use ChatGPT to identify and correct errors in code samples.
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