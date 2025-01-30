snow_bows = int(input())

score = [0, 0, 0, 0]


for x in range(snow_bows):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > score[0]:
        score[0] = value
        score[1] = weight
        score[2] = time
        score[3] = quality

print(f"{score[1]} : {score[2]} = {score[0]:.0f} ({score[3]})")
    

