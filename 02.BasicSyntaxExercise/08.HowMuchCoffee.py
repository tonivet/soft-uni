event = input()

event_list = ["coding", "dog", "cat", "movie"]
coffee = 0

while event != "END":
    if event.lower() in event_list:
        if event.islower():
            coffee += 1
        elif event.isupper():
            coffee += 2
    
    event = input()

if coffee >= 5:
    print("You need extra sleep")
else:
    print(coffee)