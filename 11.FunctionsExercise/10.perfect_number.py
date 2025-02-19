def isPerfect(number):
    sum = 0
    if number>1:
        for divisor in range(1, number):
            if number % divisor == 0:
                sum += divisor
    if sum == number or number==1:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(isPerfect(int(input())))