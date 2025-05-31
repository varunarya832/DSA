
# nums = [5,3,2,5,7,3,6,9,5]

def buyAndSellStock(nums):

    if not nums:
        return 0

    current_buy = float('inf')

    max_profit = 0

    for i in range(len(nums)):

        if nums[i] < current_buy:
            current_buy = nums[i]

        else:
            current_sell_profit = nums[i] - current_buy

            if current_sell_profit > max_profit:
                max_profit = current_sell_profit
            else:
                continue
    
    return max_profit


print(buyAndSellStock([5,3,2,5,7,3,6,9,5]))


