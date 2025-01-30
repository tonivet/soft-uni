divisor = int(input())
boundry = int(input())

for n in range(boundry, divisor, -1):
    if n % divisor == 0:
        print(n)
        break