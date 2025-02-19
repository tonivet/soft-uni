nums = [int(x) for x in input().split(" ")]

command_input = input().split()

while command_input[0] != "Finish":
    command = command_input[0]
    value = int(command_input[1])

    if command == "Add":
        nums.append(value)
    if command == "Remove":
        if value in nums:
            nums.remove(value)
    if command == "Replace":
        if value in nums:
            x = nums.index(value)
            nums[x] = int(command_input[2])
    if command == "Collapse":
        nums = list(filter(lambda x: x>=value, nums))    
    
    command_input = input().split()

print(*nums)