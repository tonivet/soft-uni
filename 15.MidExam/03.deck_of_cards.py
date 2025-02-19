list_of_cards = input().split(", ")
num_commands = int(input())
x = 0

while x < num_commands:
    command = input().split(", ")

    if command[0] == "Add":
        if list_of_cards.count(command[1]):
            print("Card is already in the deck")
        else:
            list_of_cards.append(command[1])
            print("Card successfully added")
    if command[0] =="Remove":
        if command[1] in list_of_cards:
            list_of_cards.remove(command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    if command[0] == "Remove At":
        if int(command[1]) >= len(list_of_cards):
            print("Index out of range")
        else:
            list_of_cards.pop(int(command[1]))
            print("Card successfully removed")
    if command[0] == "Insert":
        if int(command[1]) >= len(list_of_cards) or int(command[1]) < 0:
            print("Index out of range")
        elif command[2] in list_of_cards:
            print("Card is already added")
        else:
            list_of_cards.insert(int(command[1]), command[2])
            print("Card successfully added")

    x +=1

print(", ".join(list_of_cards))

