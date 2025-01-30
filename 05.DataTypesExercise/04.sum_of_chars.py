number_of_lines = int(input())
total_sum = 0

while number_of_lines > 0:
    char = input()
    total_sum += ord(char)
    number_of_lines -= 1
else:
    print(f"The sum equals: {total_sum}")