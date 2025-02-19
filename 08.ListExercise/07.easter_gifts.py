gifts = input().split()

gift_command = input()

while gift_command != "No Money":
    gift_command = gift_command.split()

    if gift_command[0] == "OutOfStock":
        gifts = [None if item == gift_command[-1] else item for item in gifts]
    elif gift_command[0] == "Required":
        if 0 <= int(gift_command[-1]) < len(gifts):
            gifts[int(gift_command[-1])] = gift_command[1]
    elif gift_command[0] == "JustInCase":
        gifts[-1] = gift_command[-1]

    gift_command = input()
    
for item in gifts:
    if item == None:
        gifts.remove(None)

print(' '.join(gifts))