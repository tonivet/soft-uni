int_list = [int(x) for x in input().split()]
n = int(input())

remove_list = sorted(int_list)
remove_list = remove_list[:n]

for x in remove_list:
    int_list.remove(x)

print(', '.join(str(x) for x in int_list))