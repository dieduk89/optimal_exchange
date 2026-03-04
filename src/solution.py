def solve(case: str) -> str:
    lines = case.split("\n")
    n = int(lines[0])
    result = ""
    for i in range(n):
        values = list(map(int, lines[i + 1].split(" ")))
        k, size, coins = values[0], values[1], values[2:]
        coins.sort()
        print(f"Item {i + 1}: {k}, {size}, {coins}")
        print("\n")
        optimal_exchange = find_optimal_exchange(k, size, coins)
        result += optimal_exchange
    return result

def find_optimal_exchange(k: int, size: int, coins: list[int]) -> str:
    optimals_values = [i + 1 if i + 1 not in coins else 1 for i in range(k)]
    for i in range(k):
        optimals_values[i] = calculate_optimal_exchanges(optimals_values, i + 1, coins)
    #print(f"Optimals values: {optimals_values}")
    avg_value = round(sum(optimals_values) / len(optimals_values), 2)
    max_value = max(optimals_values)
    print(f"Avg value: {avg_value}") 
    print(f"Max value: {max_value}")
    return f"{avg_value} {max_value}\n"


def calculate_optimal_exchanges(optimals_values: list[int], x: int, coins: list[int]) -> int:
    exchanges = [optimals_values[x - 1]]
    for coin in coins:
        diff = abs(coin - x)
        exchanges.append(optimals_values[diff - 1] + 1)
    #print(f"Exchanges for {x}: {exchanges}")
    #print("\n")
    return min(exchanges)

   