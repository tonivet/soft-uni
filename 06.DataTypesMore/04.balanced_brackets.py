n = int(input())
openingbrace = 0
closingbrace = 0
opening = False
for i in range(n):
    newstring = input()
    if newstring == "(":
        openingbrace += 1
        opening = True
    elif newstring == ")" and opening == True:
        closingbrace += 1
        opening = False
if openingbrace == closingbrace:
    print('BALANCED')
else:
    print('UNBALANCED')