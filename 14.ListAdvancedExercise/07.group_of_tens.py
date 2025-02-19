nums = [int(x) for x in input().split(", ")]

group_num = 0

while nums:
    group_num += 10
    groups = list(filter(lambda x: x <= group_num, nums ))
    nums = list(set(nums) - set(groups))
    print(f"Group of {group_num}'s: {groups}")