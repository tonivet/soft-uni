nums = [int(x) for x in input().split(', ')]
beggar = int(input())

num_sum = [0 for x in range(beggar)]
start_beg = 0

for x in nums:
    num_sum[start_beg] += x
    start_beg += 1
    if start_beg >= beggar:
        start_beg = 0


print(num_sum)
