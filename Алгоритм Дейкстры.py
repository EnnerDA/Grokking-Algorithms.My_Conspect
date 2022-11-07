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
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# создаём хэш-таблицу родителей
parents = {}
parents['start'] = None
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# cоздаём список для учета отработаных узлов 
processed = []

def sort_dir(u_d):
    # функция возвращает список с клучами словаря, которые отсортированны в поряде увеличения их значений 
    sort_list = []
    for key in u_d:
        if len(sort_list) == 0:
            sort_list.append(key)
        else:
            if u_d[key] > u_d[sort_list[-1]]:
                sort_list.append(key)
            else:
                for n in range(len(sort_list)):
                    if u_d[key] <= u_d[sort_list[n]]:
                        sort_list.insert(n, key)
                        break
                    else:
                        None
    return sort_list    
    
def calculate_graph(node):
    # функция решает весь граф перезаписывая словари "parents" и "costs"
    for neighbor in sort_dir(graph[node]):
        for n in sort_dir(graph[neighbor]):
            if costs[n] > costs[neighbor] + graph[neighbor][n]:
                costs[n] = costs[neighbor] + graph[neighbor][n]
                parents[n] = neighbor
            else:
                None
        for next_node in sort_dir(graph[node]):
            if next_node in processed:
                None
            else:
                calculate_graph(next_node) #рекурсия
                processed.append(next_node)
        
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
calculate_graph('start')
graph_way('end')
