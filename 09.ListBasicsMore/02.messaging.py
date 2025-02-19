num_index = input().split()
str_line = input()

new_index = []
new_line = ''

for element in num_index:
    x = sum(int(i) for i in element)
    new_index.append(x)

for num in new_index:
    if num < len(str_line):
        new_line += str_line[num]
        str_line = str_line[:num] + str_line[num+1:]
    elif num > len(str_line):
        while num > len(str_line):
            num -= len(str_line)
        new_line += str_line[num]
        str_line = str_line[:num] + str_line[num+1:]

print(new_line)
