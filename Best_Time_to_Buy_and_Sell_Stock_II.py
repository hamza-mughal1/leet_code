def foo(prices):
    l = 0
    maximum = 0
    if len(prices) <= 1:
        return maximum
    for r in range(1,len(prices)):
        if prices[r] < prices[l]:
            l = r
        if prices[l] < prices[r]:
            maximum += prices[r]-prices[l]
            l = r
        
    return maximum