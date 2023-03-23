n, m, a = map(int, input().split())

width = n // a

if n % a > 0:
    width = width + 1

height = m // a

if m % a > 0:
    height = height + 1

Theatre_Square = width * height

print(Theatre_Square)