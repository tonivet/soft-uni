num_rooms = int(input())

free_chairs = 0
need_chairs = False
for room in range(num_rooms):
    chair_visitor = input().split(" ")
    if len(chair_visitor[0]) < int(chair_visitor[1]):
        chair = int(chair_visitor[1]) - len(chair_visitor[0])
        print(f"{chair} more chairs needed in room {room + 1}")
        need_chairs = True
    else:
        free_chairs +=1
if not need_chairs:
    print(f"Game On, {free_chairs} free chairs left")