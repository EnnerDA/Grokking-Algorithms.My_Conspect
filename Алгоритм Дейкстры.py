#создаём хэш-таблицу графа
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['start']['c'] = 5
graph['start']['d'] = 8
graph['start']['e'] = 10
graph['start']['f'] = 12

graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

# создаём хэш-таблицу стоимостей узла
infinity = float('inf') #бесконечность
costs = {}
costs['start'] = 0
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# создаём хэш-таблицу родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

#Создаём список для учета отработаных узлов 
processed = []

def find_lowest_cost_node(node):
    if graph[node] == {}:
        return None
    else:
        lowest_cost = infinity
        for neighbour in graph[node]: 
            if graph[node][neighbour] < lowest_cost and neighbour not in processed:
                lowest_cost = graph[node][neighbour]
                n = neighbour
            if costs[n] > graph[node][n] + costs[node]:
                costs[n] = graph[node][n] + costs[node]
                parents[n] = node
        return n        
        
# GO GO GO !
node = 'start'
while node != 'end':
    node = find_lowest_cost_node(node)

way =node
while way != 'start':
    print(parents[way])
    way = parents[way]
