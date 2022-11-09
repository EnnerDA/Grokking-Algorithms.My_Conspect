import copy

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
    
def calculate_graph(nobe):
    # функция просчитывает граф обновляя словари parents и costs для всех узлов
    nobe_list = sort_dir(graph[nobe])
    new_nobe_list = copy.copy(nobe_list)
    new_nobe_dir = {}

    while nobe_list != []:
        for neighbor in graph[nobe_list[0]].keys(): # nobe_list[0] - рассматриваемый нами узел
            if costs[neighbor] > costs[nobe_list[0]] + graph[nobe_list[0]][neighbor]:
                costs[neighbor] = costs[nobe_list[0]] + graph[nobe_list[0]][neighbor]
                parents[neighbor] = nobe_list[0]
            else:
                None
            if neighbor not in new_nobe_list and neighbor not in processed:
                new_nobe_list.append(neighbor)
                new_nobe_dir[neighbor] = costs[neighbor]

        processed.append(nobe_list.pop(0))
        nobe_list += sort_dir(new_nobe_dir)
        new_nobe_dir = {}

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


# GO! Go! go!
calculate_graph('start')
graph_way('end')

