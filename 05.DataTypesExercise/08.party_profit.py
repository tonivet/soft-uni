group_size = int(input())
days = int(input())

coins = 0
x = 0 

while days != 0:
    x += 1
    
    if x % 10 == 0:
        group_size -= 2
    if x % 15 == 0:
        group_size += 5
    
    coins += 50 - group_size * 2

    if x % 3 == 0:
        coins -= group_size * 3
    if x % 5 == 0:
        coins += 20 * group_size
        if x % 3 == 0:
            coins -= group_size * 2

    days -= 1

print(f"{group_size} companions received {coins // group_size} coins each.")