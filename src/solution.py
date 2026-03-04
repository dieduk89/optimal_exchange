
def solve(case: str) -> str:
    lines = case.split("\n")
    n = int(lines[0])
    results = []
    for i in range(n):
        print("\n") 
        values = list(map(int, lines[i + 1].split(" ")))
        k, size, coins = values[0], values[1], values[2:]
        coins.sort()
        print(f"Item {i + 1}: {k}, {size}, {coins}")
        optimal_exchange = find_optimal_exchange(k, size, coins)
        results.append(optimal_exchange) 
    return "\n".join(results)

def find_optimal_exchangeV2(k: int, size: int, coins: list[int]) -> str:
    optimals_values = [1 if i + 1 in coins else 0 for i in range(k)]
    zeros = optimals_values.count(0)
    max_value = 1

    while zeros > 0:
        max_value += 1
        x = 1
        y = max_value - x
        values_to_update = set()
        while x <= y:
            #find all posible values of k for x
            xlist = [i + 1 for i in range(k) if optimals_values[i] == x]
            #find all posible values of k for y
            ylist = [i + 1 for i in range(k) if optimals_values[i] == y]
            #find all posible values of k for x + y
            values1 = (xval + yval for xval in xlist for yval in ylist if xval + yval <= k)
            #find all posible values of k for |x - y|
            values2 = (abs(xval - yval) for xval in xlist for yval in ylist if abs(xval - yval) >= 1)
            #filter values for optimals_values
            values = (v for v in set(values1) | set(values2) if optimals_values[v - 1] == 0)
            values_to_update.update(values)
            x += 1
            y = max_value - x     

        for val in values_to_update:
            optimals_values[val - 1] = max_value
    
        zeros = optimals_values.count(0)

    avg_value = round(sum(optimals_values) / len(optimals_values), 2)

    print(f"Avg value: {avg_value}") 
    print(f"Max value: {max_value}")

    return f"{avg_value} {max_value}"

    

   