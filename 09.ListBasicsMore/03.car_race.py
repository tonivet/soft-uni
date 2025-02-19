race = [int(x) for x in input().split(" ")]

middle = len(race) // 2

fst_car = race[:middle]
snd_car = race[middle+1:]
snd_car.reverse()

def calculate_time(laps):
    lap_time = 0
    for x in laps:
        if x == 0:
            lap_time *= 0.8
        lap_time += x
    return lap_time


fst_car_time = calculate_time(fst_car)
snd_car_time = calculate_time(snd_car)

print(f"The winner is left with total time: {fst_car_time:.1f}") \
if fst_car_time < snd_car_time else \
print(f"The winner is right with total time: {snd_car_time:.1f}")
