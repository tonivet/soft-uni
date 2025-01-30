
# number = list(number)
# number.sort(reverse=True)

# print(''.join(number))

# print(sorted(number, reverse=True))

number = input()

sorted_number = ''

while number != '':
    y = max(number)
    sorted_number += y
    x = number.find(y)
    number = number[:x] + number[x+1:]
else:
    print(sorted_number)



