#создаём хэш-таблицу графа
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

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

def calculate_graph(graph):
    for node in graph.keys():   #начинаем перебирать все узлы
        if node in processed:  #если узел проверен, то ничего
            None        
        else:   #а если не проверен, то
            for neighbour in graph[node]:   #начнем перебирать соседей этого узла
                if costs[neighbour] > costs[node] + graph[node][neighbour]: #оцениваем стоимость соседа
                    costs[neighbour] = costs[node] + graph[node][neighbour]
                    parents[neighbour] = node
        processed.append(node) 

# GO! Go! go!
calculate_graph(graph)
