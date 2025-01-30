budget = float(input())
flour_price = float(input())


egg_price = flour_price * 0.75
milk_price = flour_price * 1.25


loaves_price = flour_price + egg_price + (milk_price / 4)

colored_eggs = 0
current_bread_count = 0

while budget > loaves_price:
    current_bread_count += 1
    budget -= loaves_price
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        easter_lose = current_bread_count - 2
        colored_eggs -= easter_lose
else:
    print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


