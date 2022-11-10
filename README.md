# Адитья Бхаргава. Грокаем алгоритмы. Конспект книги

## Глава 1. Знакомство с алгоритмами    

_Алгоритм - набор операций для выполнения определенной задачи_    

### Бинарный поиск

Простой поиск - перебор всех элементов списка.    
Бинарный поиск  - отсекание половины неверных значений за счет сравнения с центральным элементом упорядоченного списка.   

_Логорифм - операция обратная возведению в степень_ 
_10*\*2 = 100 <-> lg100=2, тут lg - логорифм по основанию 10_
_далее log это по умолчанию логорифм по основанию 2_

Бинарный поиск работает только в отсортированных списках естественно.   

**Функция binary_search**
```python   
def binary_search(user_list, item):
    low = 0
    high = len(user_list)-1
    while low <= high:
        mid = int((low+high)/2) #в книге явно ошибка, деление на 2 необходимо
        guess = user_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        elif guess < item:
            low = mid + 1
        else:
            return None
```
[Упражнения Главы 1](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_1%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

#### "О-большое"

"О-большое" - сообщает о скорости работы алгоритма, указывая количество опреаций, как функцию от количества элементов списка.       
Типичные примеры "О-большого": 
* O(log(n)) - логорифмическое время, например для бинарного поиска.
* O(n) - линейное время, напрмиер, для простого поиска перебором.
* O(n*log(n)) - эфективные алгоритмы сортировки, тут ссылка на главу 4
* O(n*\*2) - медленные алгоритмы сортировкиб тут сслыка на главу 2
* O(n!)

[Упражнения Главы 1](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_1%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

"Задача о комивояжоре" классическая задача решение которой алгоритм решения которой имеет **О(n!)**: у Вас есть n населенных пунктов, которые вы должны посетить. Составте самый короткий маршрут. Если решать перебором всех вариантов то уже при 8 городах будет более 40 тысяч !!! вариантов маршрута. 

### Итоги Главы 1

  1. Бинарный поиск быстрее простого
  2. Время выполнения O(log(n)) быстрее O(n)
  3. Скорость алгоритмов не измеряется в секундах
  4. Время выполнения алгоритма описывается ростом количества операций.
  5. "О-большое" - это время выполнения алгоритмов. 

## Глава 2. Сортировка выбором.

**Массивы и связанные списки**

  **Массив** - четко определенное место в памяти, обратится можно к любой ячейке за одно действие. Но сложности возникают в размещении, так как ячейки должны быть рядом с друг другом. так же сложности возникают при расширении массива. Пример с группой людей желающих посмотреть кино в пятером. Им наодо 5 мест рядом. Затем приходит шестой и гурппе приходится перемещаться. 

  **Связанные списки** - это данные организованные по цепочке, в предыдущем элементе содержится ссылка на адрес следующего. Таким образом, удобно рамещать произвольные объемы данных не переживая за свободу соседних ячеек. Однако что бы обратится к i-тому элементу нам надо пройти всю цепочку с первого, чтобы получить адрес второго, третьего и т.д. до i-того. 

Время выполнения основных операций с массивами и списками.

|   | Массивы | Списки|
|---|---|---|
|Чтение | O(1) | O(n)|
|Вставка| O(n) | O(1) |
|Удаление| O(n) | O(1) |

где O(n) - линейное время, а O(1) - постоянное 

*Но вообще давольно странное утверждение. Если вставлять ячейку в список, то по идее надо сначала добраться до предидущего элемента и поменять в нем ссылку на следующий, а что б до него добраться надо перебрать всю цепочку сначала. И получается что для списка операция Вставка/Удаление имеет O(n+1).*

[Упражнения Главы 2](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_2%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

Сортировка выбором - создание нового списка, изначально пустого, далее проход по всем элементам искомого списка в поисках элемента с нужным значением (меньшим, большим ну или каковы условия) найдя нужный элемент мы помещаемего в новый список и исключаем из искомого, затем повторяем операцию поиска следующего элемента. получается в списке из n элементов, необходимо провести n + (n-1) + (n-2) + ... + (n - (n-1)) = 1/2n\*\*2. Получаем O(1/2\*n\*\*2). Но коэфициенты оказывается игнорируются при подсчете О-большого. И получаем время работы алгоритма сортировки выбором O(n\*\*2).

**Пример кода**

Функция поиска наименьшего элемента в списке:

```python
def find_smallest(user_list):
    smallest = user_list[0]
    smallest_index = 0
    for i in range(len(user_list)):
        if user_list[i] < smallest:
            smallest = user_list[i]
            smallest_index = i
    return smallest_index
```

Функция сортировки выбором:
```python
def selection_sort(user_list):
    new_user_list = []
    for i in range(len(user_list)):
        smallest_index = find_smallest(user_list)
        new_user_list.append(user_list.pop(smallest_index))
    return new_user_list
```
### Итоги Главы 2

* Память компуктера - огромный шкаф с ящиками
* Хранить элементы можно массивом или списком
* Массив - все элементы рядом. Обеспечивает быстрое чтение.
* Список - цепочка, элементы распределены в произвольных местах, в каждом элементе храниться адрес следующего. Списки обеспечивают быструю вставку.
* Элементы массива должны быть одноипны. *Ежле чесно не понял почему этио?*

## Глава 3. Рекурсия.

**Рекурсия**
Пример задачи: нужно найти ключ, он в коробке, но в коробке есть коробки в которых могут быть коробки поменьше, ключ может быть в любой из них. Есть два варианта решения:

![изображение](https://user-images.githubusercontent.com/116806816/198579537-43db5e30-2ac1-4565-9a79-44f5bb785f76.png)

```python
def look_for_key(main_box): 	
    pile = main_box.make_a_pile_to_look_through() 	
     while pile is not empty: 	
        Ьох = pile.grab_a_box() 	
        for item in Ьох: 	
            if item.is_a_box(): 	
                pile.append(item) 	
            elif item.is_a_key(): 	
                print "found the key!"
```
Для рекурсии это выглядит так:
```python
def look_for_key(bох): 	
    for item in Ьох: 	
        if item == box: 	
            look_for_key(item)	#РЕКУРСИЯ MOMENT!!!
        elif item == key(): 	
            print "found the key!"
```

**Стек вызовов**

**Стек** - упорядоченный список, очередь задач.

[Упражнения Главы 3](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0%203%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

### Итоги Главы 3.

* Когда функция вызывает саму себя, это называется рекурсией.
* В каждой рекурсивной функции должно быть два случая: базовый и рекурсивный .
* Стек поддерживает две операции: занесение и извлечение элементов.
* Все вызовы функций сохраняются в стеке вызовов.
* Если стек вызовов станет очень большим, он займет слишком много памяти.

## Глава 4. Быстрая сортировка.

**Принцип "Разделяй и властвуй"**
Принцип состоит из двух действий:
1. Определить простейщий базовый случай.
2. Придумать, как свести задачу к базовому случаю. 

Пример алгоритма Евклида для поиска наибольшего гбщего делителя двух чисел. [Вот кстати я написал этот алгоритм с рекурсией.](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/evklid_it.py)

>**Совет**
>
>Когда вы пишете рекурсивную функцию, в которой задействован массив, базовым случаем часто оказывается пустой массив или массив из одного элемента. Если вы не знаете, с чего начать, - начните с этого.

[Упражнения Главы 4](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0%204%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

**Сортировка слиянием и быстрая сортировка**

**Быстрая сортировка** - выбор опорного элемента и разделение списка на две части слева и справа от опорного (больше опорного или меньше опорного), далее каждую часть рекурсивно разбивают на две части и опорный элемент и т.д до базового случая. Базовым является массив из двух элементов, их отсортировать совсем не сложно!

**Сортировка слиянием** это три этапа, выглядит так:

1. Сортируемый массив разбивается на две части примерно одинакового размера;
2. Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
3. Два упорядоченных массива половинного размера соединяются в один.
Половины массива разбиваются пополам, те в свою очередь еще пополам пока не достигнут базового случая - в массиве один или ноль элементов. 

```python
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:]) 
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A
```

Очень неявная история с тем, что при поочередном переборе элементов массива с убиранием одного элемента на каждом шаге скорость операции всегда одинакова и равна O(n). Странно я это не понял, каждый раз элементов становиться меньше и по мне дык скорость должна быть O(n-i), где i - порядковый номер итерации. Ну да ладно простим автору моё не понимание.

[Упражнения Главы 4](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0%204%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

### Итоги главы 4

* Стратегия "Разделяй и властвуй" - разбиение задачи на уменьшающиеся фрагменты сводящиеся к базовому случаю. Со списком базовым случаем как правило является пустой массив или массив из одного элемента.
* Если используете алгоритм быстрой сортировки, то в качестве опорного элемента выбирайте случайный элемент! Среднее время быстрой сортировки составит O(n\*log(n)).
* Константы "О-большого" иногда имеют значение. По этой причине быстрая сортировка быстрее соритировки слиянием.

_На вский случай для себя отмечу, быстрая сортировка - выбор опорного элемента и распределение всех чисел относительно него влево и вправо, далее рекурсия до базы._

_А сортировка слиянием просто рекурсивное деление массива на половины до базы, без опорного._

_И та и другая сортирвки имеют время O(n\*log(n))_

* при сравнении простой сортировки и бинарной константа роли не играет ибо O(log(n)) слишком сильно превосходит O(n) по скорости при большом размере списка.

## Глава 5. Хэш-таблицы.

Хэш-функция это как шифровшик, зная размер массива она преводит слова в цифры, которые являются номером ячейки в массиве. Таким образом, что бы поместить запомнить связанную пару информации, например, "апельсин - 16 руб." мы передаём хэш-функции "апельсин", она выдаёт нам "4", и мы загружаем в 4 ячейку массива значение "16 руб". Что получили? В случае поиска "апельсин" мы за время O(1) получим "16 руб".

[Упражения Главы 5](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_5%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

Кэширование - запоминание данных. Кэшируемые данные хранятся в хэше.

**Коллизии**
Ввиду ограниченного размера массива для хэш-таблицы, в одну ячейку могут попасть два и более значения, тогда в ячейку хэш-тфблицы будет помещен список. Быстродействие при обрашении в эту ячейку естественно снизится. 

Идеельная хэш-функция распределяет значения равномерно по всему хэшу, и создаёт минимальное число коллизий.

**Быстродействие хэш-таблицы**

|   | Средний случай | Худший случай|
|---|---|---|
|Поиск | O(1) | O(n)|
|Вставка| O(1) | O(n) |
|Удаление| O(1) | O(n) |

вспомним
|   | Массивы | Списки|
|---|---|---|
|Поиск | O(1) | O(n)|
|Вставка| O(n) | O(1) |
|Удаление| O(n) | O(1) |

Что бы приблизить большую часть запросов к "средним случаям" нужен:
* низкий коэфициент заполнения 
* хорошая хэш-функция

[Упражения Главы 5](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_5%20%D1%83%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

### Итоги Главы 5

* Хэш-таблица это объединение хэш-функций с массивом.
* Коллизии нежелательны.
* Хэш-таблицы обеспечивают очень быстрое выполнение поиска, вставки и удаления.
* Хэш-таблицы хоршо подходят для моделирования отношений между объектами.
* Когда коэффициент заполнения таблицы превышает 0,7 ее пора расширять.
* Хэш-таблицы используются для кэширования данных (например на вэб-серверах).
* Хэш-таблицы хорошо подходят для обнаружения дубликатов.

## Глава 6. Поиск в ширину.

Алгоритм для решения задачи поиска кратчайшего пути называется поиском в ширину.

Граф — математическая абстракция реальной системы любой природы, объекты которой обладают парными связями. Граф как математический объект есть совокупность двух множеств — множества самих объектов, называемого множеством вершин, и множества их парных связей, называемого множеством рёбер. Элемент множества рёбер есть пара элементов множества вершин. 

Связи первого уровня предпочтительнее связей второго уровня, связи второго уровня предпочтительнее связей третьего уровня и т. д. Отсюда следует, что поиск по контактам второго уровня не должен производиться, пока вы не будете полностью уверены в том, что среди связей первого уровня нет ни одного продавца манго.

Очередь относится к категории структур данных FIFO: First In , First Out («первым вошел, первым вышел»). А стек принадлежит к числу структур данных LIFO: Last In , First Out («последним пришел , первым вышел»).

[Упражнения Главы 6](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_6%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

Самый простой граф на Python
```python
graph = {}
graph["you"] = ["alice", "ЬоЬ", "claire"]
```
Графы бывают направленные и ненаправленные.

Пример графа и его реализации на Python
![Graph](https://user-images.githubusercontent.com/116806816/199453525-be3bb4f1-394d-4bc8-9462-c264ead90852.png)

```python
from collections import deque

def search(name):
    search_queue = deque() #создание очереди
    search_queue += graph[name] #добавление первого графа
    searched = [] # создание списка уже проверенных
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person.title(), 'is a seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #добавление в список проверенных
        
        
def person_is_seller(person):
    if person in seller_list:
        return True
    else:
        return False

seller_list = ['thom']

graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search('you')
```

### Итоги Главы 6. 

* Поиск в ширину позволяет определить существует ли путь из А в В.
* Если путь существует, то поиск в ширину находит кратчайщий путь.
* Очереди относятся к категории FIFO («первым вошел, первым вышел»).
* Стек относится к категории LIFO («последним пришел, первым вышел»).
* Список поиска должен быть очередью, иначе найденый путь не будет кратчайщим.
* Проверенный элемент не должен проверятся заново, иначе поиск стать бесконечным.

## Глава 7. Алгоритмы Дейкстры.

Алгоритм Дейкстры:
1. Найти узел с наименьшей стоимостью (то есть узел, до которого можно добраться за минимальное время).
2. Обновить стоимости соседей этого узла.
3. Повторять, пока это не будет сделано для всех узлов графа.
4. Вычислить итоговый путь.

Для визуализации алгоритма Дейкстры используем таблицу

![изображение](https://user-images.githubusercontent.com/116806816/199473578-b147dd79-5bcb-49c2-bbee-7f87fbe11d0d.png)


Использование алгоритма Дейкстры графом, с содержащим ребра с отрицательным весом, невозможно. Если вы хотите найти кратчайший путь в графе, содержащем ребра с отрицательным весом, для этого существует специальный алгоритм, называемый алгоритмом Беллмана- Форда.

Реализация алгоритма Дейкстры на Python

![изображение](https://user-images.githubusercontent.com/116806816/199480491-9a140126-183e-47e6-8aa5-01ce4771ba9f.png)
```python
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
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

#Создаём список для учета отработаных узлов
processed = []

# GO GO GO !

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
```
[моя версия алгоритма Дейкстры](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%D0%94%D0%B5%D0%B9%D0%BA%D1%81%D1%82%D1%80%D1%8B.py)

[Упражнения Главы 7](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_7%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

### Итоги Главы 7:

 * Поиск в ширину вычисляет кратчайщий путь в невзвешенном графе.
 * Алгоритм Дейкстры высчисляет кратчайщий путь во взвешенном графе.
 * Алгоритм Дейкстры работает только с положительными значениями веса. _Если вернешься к этому пункту проверь еще разик это утверждение_
 * При наличии отрицательных весов используйте алгоритм Беллмана-Форда.
 ---
 
 ## Глава 8. Жадные алгоритмы.
 
 Жадный алгоритм - на каждом шаге выбирать вариант с наилучшее значение без оглядки на дальнейщие шаги.
 
 [Упражнения главы 8](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_8%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)
 
Уж не знаю почему, но код в этой книге крайне труден для усвоения посему в задачи на покрытие штатов радиостанциями действовать будем сами. 

ДАНО:
``` pytnoh
stations = {} 	
stations["kone"] = set(["id", "nv", "ut"]) 	
stations["ktwo"] = set(["wa", "id", "mt"]) 	
stations["kthree"] = set(["or", "nv", "са"]) 	
stations["kfour"] = set(["nv", "ut"]) 	
stations["kfive"] = set(["ca", "az"])	
```
Создадим перечень нужных штатов:
```python
for states in stations.values():
    for stat in states:
        states_needed.append(stat)
states_needed = set(states_needed)
```
Ну и найдём жадным алгоритмом станции которые покрывают вообще всё
```python
while len(states_needed) != 0:
    best_station = None 			
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(states_covered) < len(covered):
            states_covered = covered
            best_station = station
            use_stantion.append(best_station)
    states_needed = states_needed - states_covered
print(use_stantion)
```
Результат
```
['kone', 'ktwo', 'kthree', 'kfive']
```
что собственно совпадает с книгой.

[Упражнения главы 8](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_8%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

### NP-полные задачи
Несколько характерных признаков NP-полной задачи: 	
* ваш алгоритм быстро работает при малом количестве элементов, но сильно замедляется при увеличении их числа; 	
* формулировка "все комбинации х" часто указывает на NР-полноту задачи; 	
* вам приходится вычислять все возможные варианты Х, потому что задачу невозможно разбить на меньшие подзадачи? Такая задача может оказаться NР-полной; 	
* если в задаче встречается некоторая последовательность (например, последовательность городов, как в задаче о коммивояжере) и задача не имеет простого решения, она может оказаться NР-полной; 	
* если в задаче встречается некоторое множество (например, множество радиостанций) и задача не имеет простого решения, она может оказаться NР-полной; 	
* можно ли переформулировать задачу в условиях задачи покрытия множества или задачи о коммивояжере? В таком случае ваша задача определенно является NР-полной.	

## Итоги главы 8

* Жадные алгоритмы стремятся к локальной оптимизации в расчете на то, что в итоге будет достигнут глобальный оптимум. 	
* У NР-полных задач не существует известных быстрых решений. 	
* Если у вас имеется NР-полная задача, лучше всего воспользоваться приближенным алгоритмом. 	
* Жадные алгоритмы легко реализуются и быстро выполняются, поэтому из них получаются хорошие приближенные алгоритмы.	
---
## Глава 9. Динамическое програмирование.

Динамическое програмирование  - метод решения сложных задач, разбиванием на подзадачи, которые решаются в первую очередь.

Рисуем таблицу аргументов и их стоимостей

![изображение](https://user-images.githubusercontent.com/116806816/201027541-5f4c10fa-eb71-417e-9d0e-e98359679571.png)

и заполняем ее с помощью формулы

![изображение](https://user-images.githubusercontent.com/116806816/201027700-4cb5b61e-d73a-49f1-9d5b-700cd1fce93c.png)

В результате правый нижний угол дал нам полный ответ, все отсальные ячейки таблицы - процесс динамического програмирования.

[Упражнения Главы 9](https://github.com/EnnerDA/Grokking-Algorithms.My_Conspect/blob/main/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_9%20%D0%A3%D0%BF%D1%80%D0%B0%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F.md)

А вот код для проверки слов: 

```python
word_a = 'fish'
word_b = 'vista'
x = []
cell = []
max_cell = 0
j_string = []
for j in range(len(word_b)):
    j_string.append(0)

for i in range(len(word_a)):
    cell.append(j_string)

for i in range(0, len(word_a)-1):
    for j in range(0, len(word_b)-1):
        if word_a[i] == word_b[j]:
            max_cell += 1
            cell[i][j] = max_cell
        else:
            print(f'i = {i}, j = {j}')
            print(f' word_a[i] = {word_a[i]}, word_b[j] = {word_b[j]}')
            cell[i][j] = max_cell
```
### Итоги Главы 9

* Динамическое программирование применяется при оптимизации некоторой характеристики.
* Динамическое программирование работает только в ситуациях, в которых задача может быть разбита на автономные подзадачи.
* В каждом решении из области динамического программирования строится таблица.
* Значения ячеек таблицы обычно соответствуют оптимизируемой характеристике.
* Каждая ячейка представляет подзадачу, поэтому вы должны подумать о том, как разбить задачу на подзадачи.
* Не существует единой формулы для вычисления решений методом динамического программирования.
---
## Глава 10 Алгоритм k ближайших соседей.

```



