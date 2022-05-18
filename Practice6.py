# Multiplication table generator
x = 0
while x < 13:
    x += 1
    for i in range(1,13):
        print(i, "x", x, "=", i*x)
    print()
