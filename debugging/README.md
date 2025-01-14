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

```bash
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
```


### 1. Debugging - Python Arguments

#### Objectives
- Fix the code, it should print only the arguments without the python file name.
- Code to fix :

```bash
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])

#### Expected result
➜  debugging git:(main) ✗ ./print_arguments.py 5
Liste des arguments passés au script :
Argument 0 : ./print_arguments.py
Argument 1 : 5
```


### 2. Debugging - HTML / Javascript

#### Objectives
- Fix the code, it should change the background color when you click on the button.


### 3. Debugging - Python Mines

#### Objectives
- Fix the code, implement a mechanism to detect when all non-mine cells have been revealed, thus winning the game.

#### Game Overview
- Minesweeper is a puzzle game where the player must clear a field of hidden “mines” without detonating any of them, using clues about the number of neighboring mines in each field.

#### Expected result
➜  debugging git:(main) ✗ ./mines.py 

  0 1 2 3 4 5 6 7 8 9
0 . . . . . . . . . . 
1 . . . . . . . . . . 
2 . . . . . . . . . . 
3 . . . . . . . . . . 
4 . . . . . . . . . . 
5 . . . . . . . . . . 
6 . . . . . . . . . . 
7 . . . . . . . . . . 
8 . . . . . . . . . . 
9 . . . . . . . . . . 
Enter x coordinate:
Enter y coordinate:


### 4. Documentation - Python Factorial

#### Objectives
- Use ChatGPT to document the code
- Add the comments to this code. You should have 3 sections: function description, parameters and returns.



### 5. Error Handling - Python Checkbook

#### Objectives
- Use ChatGPT to document the code
- Fix the code, to prevent the program from crashing due to invalid input (e.g., non-numeric values), add error handling mechanisms.


### 6. Debugging - Tic Tac Toe Python

#### Objectives
- Use ChatGPT to identify and correct errors in code samples. (There may be several errors on the code)

#### Game Overview
- Players alternate placing “X” or “O” on a 3x3 board, aiming to get three in a row horizontally, vertically, or diagonally to win.

#### Expected result
- debugging git:(main) ./tic.py 
  |   |  
-----
  |   |  
-----
  |   |  
-----