n = int(input())

not_pure = [',', '.', '_']

for _ in range(n):
    sentence = list(input())
    if set(sentence) & set(not_pure):
        print(f"{''.join(sentence)} is not pure!")
    else:
        print(f"{''.join(sentence)} is pure.")

