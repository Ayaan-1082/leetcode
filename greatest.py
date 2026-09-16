# greatest.py
import sys

try:
    if len(sys.argv) == 4:
        a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        print(f"Inputs: a={a}, b={b}, c={c}")
    else:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
except EOFError:
    a, b, c = 5, 10, 3
    print(f"No input detected. Using defaults: {a}, {b}, {c}")

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The greatest number is: {largest}")
