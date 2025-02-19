herd = input().split(', ')

wolf = herd.index('wolf')

if wolf == len(herd)-1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(herd) - 1 - wolf}! You are about to be eaten by a wolf!")