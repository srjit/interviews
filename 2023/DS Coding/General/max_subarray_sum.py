


def max_subarray_sum(prices):

    max_profit = 0
    lowest_price = prices[0]
    for current_price in prices[1:]:
      max_profit = max(current_price - lowest_price, max_profit)
      lowest_price = min(lowest_price, current_price)
      
    return max_profit


def max_profit(prices):
  
  min_price = prices[0]
  max_profit = 0
  for cur_price in prices[1:]:
    max_profit = max(max_profit, cur_price - min_price)
    min_price = min(min_price, cur_price)
    
  return max_profit

print(max_subarray_sum([9, 1, 3, 6, 4, 8, 3, 5, 5]))
print(max_profit([9, 1, 3, 6, 4, 8, 3, 5, 5]))
