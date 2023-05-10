def solve(prices):
    profit = 0
    size = len(prices)
    i = 0
    j = size - 1
    while i < j:
        currentProfit = prices[j] - prices[i]
        if currentProfit > profit:
            profit = currentProfit
        if j - i == 1:
            j = size
            i += 1

        j -= 1

    return profit


if __name__ == '__main__':
    result = solve([7, 1, 5, 3, 6, 4])
    print(result)
