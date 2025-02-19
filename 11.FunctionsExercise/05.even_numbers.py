num_input = input().split()

def even_nums(num):
    even_num = []
    if int(num) % 2 == 0:
        even_num.append(int(num))
    return even_num

even_num_list = filter(even_nums, num_input)

print([int(item) for item in list(even_num_list)])