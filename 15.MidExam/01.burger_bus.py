number_of_cities = int(input())
city_count = 1
total_profit = 0

while city_count <= number_of_cities:
    city = input()
    income = float(input())
    expenses = float(input())

    if city_count % 5 == 0:
        income -= (income * 1.1) - income
    elif city_count % 3 == 0:
        expenses  *= 1.5

    profit = income - expenses
    total_profit += profit
    city_count += 1

    print(f"In {city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

