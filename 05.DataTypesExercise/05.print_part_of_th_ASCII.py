first_index = int(input())
second_index = int(input())

while first_index != second_index:
    print(chr(first_index), end=' ')
    first_index += 1
else:
    print(chr(second_index))