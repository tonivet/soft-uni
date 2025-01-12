number_of_orders = int(input())

total = 0

for _ in range(0, number_of_orders, 1):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue
    if  days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    
    price = capsule_price * days * capsules_per_day
    print(f"The price for the coffee is: ${price:.2f}")

    total += price

print(f"Total: ${total:.2f}")