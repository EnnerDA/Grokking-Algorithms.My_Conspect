# создаём хэш-таблицу графа
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['d'] = 6
graph['c']['end'] = 3

graph['d'] = {}
graph['d']['end'] = 1

graph['end'] = {}

# создаём хэш-таблицу стоимостей узла
infinity = float('inf') #бесконечность
costs = {}
costs['start'] = 0
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['end'] = infinity

# создаём хэш-таблицу родителей
parents = {}
parents['start'] = None
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['end'] = None

# cоздаём список для учета отработаных узлов 
processed = []

def calculate_graph():
    # функция просчитывает весь граф
    for node in graph.keys():   # начинаем перебирать все узлы
        if node in processed:  # если узел проверен, то ничего
            None        
        else:   # а если не проверен, то
            for neighbour in graph[node]:   # начнем перебирать соседей этого узла
                if costs[neighbour] > costs[node] + graph[node][neighbour]: # оцениваем стоимость соседа
                    costs[neighbour] = costs[node] + graph[node][neighbour]
                    parents[neighbour] = node
        processed.append(node) 

def graph_way(node):
    # функция для составления маршрута в решенном графе
    way_lisrt =''
    if parents[node] == None:
        print('  This function work correctly only on calculate graph!')
        print('  Please start calculate_graph(graph) function first.')
    else:
        way_list = node
        n = node
        while n:
            n = parents[n]
            if n == None:
                break
            way_list = n + ' --> ' + way_list
        print(f'Our way: \n\t{way_list} \nand it is costs {costs[node]} units')

#GO! Go! go!
calculate_graph()
graph_way('end')
