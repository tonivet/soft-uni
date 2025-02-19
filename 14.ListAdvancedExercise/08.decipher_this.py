sacred_code = input().split()

decode = []

for word in sacred_code:
    num = [i for i in word if i.isnumeric()]
    num = int(''.join(num))
    word = [i for i in word if not i.isnumeric()]
    word[0], word[-1] = word[-1], word[0]
    num = chr(num)
    word = num + "".join(word)
    decode.append(word)

print(*decode)