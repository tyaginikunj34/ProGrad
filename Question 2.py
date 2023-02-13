def change_calculator(amount, denominations, max_coins):
    change = []
    for coin in denominations:
        while coin <= amount and max_coins[coin] > 0:
            amount -= coin
            max_coins[coin] -= 1
            change.append(coin)
    if amount == 0:
        return change
    else:
        return None

# British Pound example
amount = 43
denominations = [1, 2, 5, 10, 20, 50]
max_coins = {1: float("inf"), 2: float("inf"), 5: float("inf"), 10: float("inf"), 20: float("inf"), 50: float("inf")}
print(change_calculator(amount, denominations, max_coins))

# US Dollar example
amount = 43
denominations = [1, 5, 10, 25]
max_coins = {1: float("inf"), 5: float("inf"), 10: float("inf"), 25: float("inf")}
print(change_calculator(amount, denominations, max_coins))

# Norwegian Krone example
amount = 43
denominations = [1, 5, 10, 20]
max_coins = {1: float("inf"), 5: float("inf"), 10: float("inf"), 20: float("inf")}
print(change_calculator(amount, denominations, max_coins))