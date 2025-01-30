quantity_decorations = int(input())
days_till_christmas = int(input())

ornament_set = (2, 5)
tree_skirt = (5, 3)
tree_garland = (3, 10)
tree_lights = (15, 17)

spirit = budget = penalty_points = 0 

if days_till_christmas % 10 == 0:
    penalty_points = 30


while days_till_christmas > 0:
    if days_till_christmas % 11 == 0:
        quantity_decorations += 2
    if days_till_christmas % 2 == 0:
        spirit += ornament_set[1]
        budget += quantity_decorations * ornament_set[0]
    if days_till_christmas % 3 == 0:
        spirit += tree_skirt[1]
        budget += quantity_decorations * tree_skirt[0]
        spirit += tree_garland[1]
        budget += quantity_decorations * tree_garland[0]
    if days_till_christmas % 5 == 0:
        spirit += tree_lights[1]
        budget += quantity_decorations * tree_lights[0]
        if (days_till_christmas % 3 == 0):
            spirit += 30
    if days_till_christmas % 10 == 0:
        spirit -= 20
        budget += tree_skirt[0]
        budget += tree_lights[0]
        budget += tree_garland[0]

    days_till_christmas -= 1
else:
    spirit -= penalty_points
    print(f"Total cost: {budget}")
    print(f"Total spirit: {spirit}")


    





