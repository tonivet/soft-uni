num = int(input())

bar = ""

for x in range(10):
    if x < int(num/10):
        bar += "%"
    else:
        bar += "."

if num == 100:
    print(f"{num}% Complete!")
    print(f"[{bar}]")
else:
    print(f"{num}% [{bar}]")
    print("Still loading...")