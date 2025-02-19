ln = [ int(item) for item in input().split(", ")]

positive = []
negative = []
even = []
odd = []

for x in ln:

    if x >= 1:
        positive.append(x)
    if x < 0:
        negative.append(x)

    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(f"Positive: {', '.join(str(x) for x in positive)}")
print(f"Negative: {', '.join(str(x) for x in negative)}")
print(f"Even: {', '.join(str(x) for x in even)}")
print(f"Odd: {', '.join(str(x) for x in odd)}")