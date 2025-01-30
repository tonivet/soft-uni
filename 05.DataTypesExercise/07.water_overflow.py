num_lines = int(input())
tank_capacity = 255
added_liters = 0

for _ in range(0, num_lines):
    add_liters = int(input())
    added_liters += add_liters
    if tank_capacity < added_liters:
        added_liters -= add_liters
        print("Insufficient capacity!")

print(added_liters)