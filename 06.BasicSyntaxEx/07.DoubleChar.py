string = input()

while not string == "End":
    if string == "SoftUni":
        pass
    else:
        print(''.join([x+x for x in string]))

    string = input()