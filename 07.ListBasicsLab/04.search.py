num = int(input())
word = input()
wrd_lst = []

for _ in range(num):
    wrd_lst.append(input())

print(wrd_lst)

for i in range(len(wrd_lst) -1, -1, -1):
    element = wrd_lst[i]
    if word not in element:
        wrd_lst.remove(element)

print(wrd_lst)