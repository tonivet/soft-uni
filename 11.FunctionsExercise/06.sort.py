num_input = input().split()

def kur(num):
    print(sorted([int(item) for item in list(num)]))

kur(num_input)