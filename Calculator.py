

import math 
from unicodedata import numeric
from math import *

Num1 = input("Number: ")
Factor = input("")
Num2 = input("Number: ")
Div ={"/", "//"}
Pow1 = ["P", "p"]
is_number = True 
Fac = ("+", "-","*",)

if (Factor in Pow1) and (Factor is not numeric):
    Num1 = int(Num1)
    Num2 = int(Num2)
elif (Factor not in Pow1) and (Factor is numeric):
    Num1 = float(Num1)
    Num2 = float(Num2)
elif (Factor not in Pow1) and (Factor is not numeric) and (Factor == ("root")):
    Num1 = float(Num1)
    Num2 = float(Num2)
elif (Factor in Fac) or (Factor in Div):
    Num1 = float(Num1)
    Num2 = float(Num2)
else: 
    is_number = False
    print("Syntax Error1")

def cubic_root(Num2):
    return round(math.exp(math.log(Num2)/3), 6)

def Pow(Num1, Num2):
    result = 1
    for number in range(Num2):
        result = result*Num1
    return result

if is_number is False:
    print("Sytnax Error2")
elif Factor == "+":
    print("Your Answer is: ", end='\n')
    print(Num1 + Num2)
elif Factor == "-":
    print("Your Answer is: ", end='\n')
    print(Num1 - Num2)
elif Factor == "*":
    print("Your Answer is: ", end='\n')
    print(Num1 * Num2)
elif Factor in Div:
    print("Your Answer is: ", end='\n')
    print(round(Num1 / Num2, 6))
elif Factor in Pow1:
    print("Your Answer is: ", end='\n')
    print(Pow(Num1, Num2))
elif (Factor == "root") and (Num1 == 2) :
    print("Your Answer is: ", end='\n')
    print(sqrt(Num2))
elif (Factor == "root") and (Num1 == 3):
    print("Your Answer is: ", end='\n')
    print(cubic_root(Num2))
else:
    print("Syntax Error3")
