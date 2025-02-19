arguments = []

for _ in range(3):
    num = int(input())
    arguments.append(num)

def subtract_fun(nums):
    num_sum = nums[0] + nums[1]
    print(num_sum - nums[2])

subtract_fun(arguments)

    