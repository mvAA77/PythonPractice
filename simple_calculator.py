num = int(input("Number: "))
oper = input("Operator:" )
num2 = int(input("Number: "))

if oper == "+" or oper == "add" or oper == "Add":
  print(num + num2)
if oper == "-" or oper == "subtraction" or oper == "Subtraction" or oper == "Minus" or oper == "minus":
  print(num - num2)
if oper == "*" or oper == "Multiplication" or oper == "multiplication" or oper == "times" or oper == "Times":
  print(num * num2)
if oper == "/" or oper == "Division" or oper == "division":
  print(num / num2)
if oper == "^" or oper == "Exponent" or oper == "exponent":
  print(num ** num2)
