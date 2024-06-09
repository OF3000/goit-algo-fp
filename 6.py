def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    res = {} 
    cost, calories = 0, 0  
    
    for item_name, item_info in sorted_items:
        if cost + item_info['cost'] <= budget:
            res[item_name] = item_info
            cost += item_info['cost']
            calories += item_info['calories']
    
    return calories, budget - cost, res

def dynamic_programming(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    for i, (item_name, item_info) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if item_info['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_info['cost']] + item_info['calories'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    res = {}
    cost = 0
    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name = list(items.keys())[i - 1]
            res[item_name] = items[item_name]
            cost += items[item_name]['cost']
            j -= items[item_name]['cost']
    
    return dp[len(items)][budget], budget - cost, res


if __name__ == "__main__":
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print('-------------------------------')
print(greedy_algorithm(items,150))
print('-------------------------------')
print(dynamic_programming(items,150))
