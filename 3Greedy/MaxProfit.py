def get_max_profit(stock_prices):
    lowest = stock_prices[0]
    highest = None

    find_potential_highest = False
    potential_lowest = None

    for price in stock_prices[1:]:
        if (find_potential_highest):
            if ((price - potential_lowest) > (highest - lowest)):
                lowest = potential_lowest
                highest = price
                find_potential_highest = False
                potential_lowest = None
        if(highest == None):
            highest = price
        if (highest < price):
            highest = price
        elif (price < lowest):
            potential_lowest = price
            find_potential_highest = True
    print(lowest, highest)

stock_prices = [10, 7, 5, 8, 11, 9]
stock_prices = [5,7,10,12,3,12,2,12,8,11,9,15, 37, 1]
# stock_prices = [8,7,6,5,4,3,2,1]
get_max_profit(stock_prices)
