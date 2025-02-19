str_inp = input()

is_alpha = []

for idx, char in enumerate(str_inp):
    if char.isupper():
        is_alpha.append(idx)

print(is_alpha)

