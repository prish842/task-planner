e = True

while e:
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
    e = input("Выйти?(да/нет) ")
    if e == "да".lower():
        break