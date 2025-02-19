nums = input().split(', ')


def palindrome_check(num_list):
    for item in num_list:
        if item == item[::-1]:
            print(True)
        else:
            print(False)

palindrome_check(nums)


