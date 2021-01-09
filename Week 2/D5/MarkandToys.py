def maximumToys(prices, k):
    prices.sort()
    count = 0
    sum = 0
    for i in range(len(prices)):
        if sum+prices[i] < k:
            sum += prices[i]
            count += 1
        else:
            return count
    return count
