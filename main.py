a = int(input())
c = input()
b = int(input())

if c == "+":
    d = a + b
elif c == "-":
    d = a - b
elif c == "*":
    d = a * b
elif c == "/":
    d = a / b
elif c == "**":
    d = a ** b
elif c == "//":
    d = a // b
elif c == "%":
    d = a % b

print(d)