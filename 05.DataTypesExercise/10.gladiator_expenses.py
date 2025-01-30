lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = lost_fights // 2
swords_broken = lost_fights // 3
shield_broken = lost_fights // 6
armor_broken = lost_fights // 6 // 2
cost = helmets_broken * helmet_price + swords_broken * sword_price + shield_broken * shield_price + armor_broken * armor_price
print(f'Gladiator expenses: {cost:.2f} aureus')