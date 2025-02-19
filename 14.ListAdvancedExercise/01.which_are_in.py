fst_lst = input().split(', ')
snd_lst = input().split(', ')

new_lst =[]

for x in fst_lst:
    for y in snd_lst:
        if y.count(x):
            if x not in new_lst:
                new_lst.append(x)

print(new_lst)