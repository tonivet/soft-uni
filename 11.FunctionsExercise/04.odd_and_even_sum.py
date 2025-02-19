num_list = input()

def sum_even_odd(nums):

    even_nums = 0
    odd_nums = 0

    for x in num_list:
        if int(x) % 2 == 0:
            even_nums += int(x)
        else:
            odd_nums += int(x)
    print(f"Odd sum = {odd_nums}, Even sum = {even_nums}")
    

sum_even_odd(num_list)