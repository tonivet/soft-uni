virus = input().split(" ")

action = input().split(" ")

new_str = ""
new_list = []

while action[0] != "3:1":
    index1 = int(action[1])
    index2 = int(action[2])
    if action[0] == "merge":
        if index1 < len(virus):
            if index2 >= len(virus):
                index2 = len(virus) - 1

            for x in range(index1, index2 + 1):
                new_str += virus[x]

            del (virus[index1:index2 + 1])
            virus.insert(index1, new_str)
            new_str = ""

    elif action[0] == "divide":
        index = int(action[1])
        part = int(action[2])
        step = len(virus[index]) // part
        word = virus[index]
        y = 0

        for x in range(step, len(word)+1, step):
            new_list.append(word[y:x])
            y=x
        virus.pop(index)
        virus = virus[:index] + new_list + virus[index:]

    action = input().split()

print(*virus)
