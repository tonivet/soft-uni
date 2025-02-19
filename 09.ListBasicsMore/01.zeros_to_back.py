zeros = [int(item) for item in input().split(', ')]

for element in zeros:
    x = zeros.index(0)
    zeros.pop(x)
    zeros.append(0)

print(zeros)