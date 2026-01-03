# Алгоритм Дейкстры. Поиск самого "дешевого" пути.
from collections import deque

graph = {}
parents = {}
costs = {}
infinity = float('inf')

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 2
graph['end'] = {}

costs['a'] = 4
costs['b'] = 3
costs['end'] = infinity

parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

processed = []

def find_lower_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

node = find_lower_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lower_cost_node(costs)

print(f'Самый дешевый путь "стоит": {costs['end']}')