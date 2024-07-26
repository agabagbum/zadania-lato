class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level   
        self.profit = profit  
        self.weight = weight  
        self.bound = bound  

def bound(node, n, W, weights, values):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight
    while j < n and total_weight + weights[j] <= W:
        total_weight += weights[j]
        profit_bound += values[j]
        j += 1
    if j < n:
        profit_bound += (W - total_weight) * values[j] / weights[j]
    return profit_bound

def knapsack_branch_and_bound(weights, values, W):
    n = len(weights)
    items = list(range(n))
    items.sort(key=lambda i: values[i]/weights[i], reverse=True)

    sorted_weights = [weights[i] for i in items]
    sorted_values = [values[i] for i in items]

    Q = []
    v = Node(-1, 0, 0, 0)
    max_profit = 0
    v.bound = bound(v, n, W, sorted_weights, sorted_values)
    Q.append(v)

    while Q:
        Q.sort(key=lambda x: x.bound, reverse=True)  
        v = Q.pop(0)

        if v.bound > max_profit:
            if v.level + 1 < n:
                u = Node(v.level + 1, v.profit + sorted_values[v.level + 1], v.weight + sorted_weights[v.level + 1], 0)
                if u.weight <= W and u.profit > max_profit:
                    max_profit = u.profit
                u.bound = bound(u, n, W, sorted_weights, sorted_values)
                if u.bound > max_profit:
                    Q.append(u)

                u = Node(v.level + 1, v.profit, v.weight, 0)
                u.bound = bound(u, n, W, sorted_weights, sorted_values)
                if u.bound > max_profit:
                    Q.append(u)

    return max_profit

if __name__ == "__main__":
    weights = list(map(int, input("Podaj wagi przedmiotów oddzielone spacjami: ").split()))
    values = list(map(int, input("Podaj wartości przedmiotów oddzielone spacjami: ").split()))
    W = int(input("Podaj całkowitą wagę plecaka: "))

    max_profit = knapsack_branch_and_bound(weights, values, W)
    print(f"Maksymalna wartość przedmiotów, które można zmieścić w plecaku: {max_profit}")
