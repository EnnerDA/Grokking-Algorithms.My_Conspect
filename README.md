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
        if item.is_a_box(): 	
            look_for_key(item)	#РЕКУРСИЯ!!!
        elif item.is_a_key(): 	
            print "found the key!"
```



