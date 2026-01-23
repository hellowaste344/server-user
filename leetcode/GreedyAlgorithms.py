Coins = [1, 5, 20, 35]
target = 148
def greedy_coin_change(coins, target):
    result = []
    for coin in sorted(Coins, reverse = True):
        while target >= coin:
            result.append(coin)
            target -= coin
    
    return result
    
selected_coins = greedy_coin_change(Coins, target)
print("Selected coins: ", selected_coins)
print("Total coins used: ", len(selected_coins))
###############################
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        
        items = []
        for v, w in zip(val, wt):
            ratio = float(v)/w
            items.append((ratio, v, w))
        
        items.sort(reverse=True)
        
        total_value = 0.0
        
        for r, v, w in items:
            if capacity == 0:
                break
            
            
            if w <= capacity:
                total_value += v
                capacity -= w
            
            else:
                fraction = float(capacity)/w
                total_value += (fraction*v)
                capacity = 0
                
        return round(total_value, 6)