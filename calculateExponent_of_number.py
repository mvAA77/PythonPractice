print("Please Enter a Number")

result = 0
num = int(input("Number: "))
exo = int(input("Exponent by 2 or 3: "))
if exo == 2:
  result = num * num

if exo == 3:
  result = num * num * num

print(result)

