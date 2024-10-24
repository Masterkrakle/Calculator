
from unicodedata import numeric


Num1 = input("Number: ")
Factor = input("")
Num2 = input("Number: ")
Div = ["/", "//"]
Pow1 = ["P", "p"]
is_number = True 
if (Factor in Pow1) and (Factor is numeric):
    Num1 = int(Num1)
    Num2 = int(Num2)
elif (Factor not in Pow1) and (Factor is numeric):
    Num1 = float(Num1)
    Num2 = float(Num2)
else: 
    is_number = False
    print("Syntax Error")

def Pow(Num1, Num2):
    result = 1
    for number in range(Num2):
        result = result*Num1
    return result

if is_number is False:
    print("Sytnax Error")
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
    print(Num1 // Num2)
elif Factor in Pow1:
    print("Your Answer is: ", end='\n')
    print(Pow(Num1, Num2))
else:
    print("Syntax Error ")
