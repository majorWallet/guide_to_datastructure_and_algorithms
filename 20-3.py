def find_greatest_profit(ar): #greedy algorithm
    buy_price = ar[0]
    greatest_profit = 0

    for price in ar:
        potential_profit = price - buy_price

        if price < buy_price:
            buy_price = price
        elif potential_profit > greatest_profit:
            greatest_profit = potential_profit
    
    return greatest_profit

print(find_greatest_profit([10,7,5,8,11,2,6]))