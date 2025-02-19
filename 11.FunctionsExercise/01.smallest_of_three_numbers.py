
def smallest_number(nums):
    nums.sort()
    print(nums[0])

arguments = []

for _ in range(3):
    num = int(input())
    arguments.append(num)

smallest_number(arguments)