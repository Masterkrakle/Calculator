
Num1 = float(input("Number: "))
Factor = input("")
Num2 = float(input("Number: "))
def Add(Num1, Num2):
    return(Num1 + Num2)
def Sub(Num1, Num2):
    return(Num1 - Num2)
def Mul(Num1, Num2):
    return(Num1*Num2)
def Div(Num1, Num2):
    return(Num1 // Num2)

if Factor == "+":
    print("Your Answer is: ", end='\n')
    print(Add(Num1, Num2))
elif Factor == "-":
    print("Your Answer is: ", end='\n')
    print(Sub(Num1, Num2))
elif Factor == "*":
    print("Your Answer is: ", end='\n')
    print(Mul(Num1, Num2))
elif Factor == "/" or "//":
    print("Your Answer is: ", end='\n')
    print(Div(Num1, Num2))
else:
    print("Syntax Error ")