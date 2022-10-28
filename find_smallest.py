def find_smallest(user_list):
    smallest = user_list[0]
    smallest_index = 0
    for i in range(len(user_list)):
        if user_list[i] < smallest:
            smallest = user_list[i]
            smallest_index = i
    return smallest_index

"""
#TEST function

from random import randint
user_list = []
for x in range(0, 11):
    user_list.append(randint(1,100))
print(user_list)
print(f'индекс элемента с минимальным значением - {find_smallest(user_list)} \nего значение -  {user_list[find_smallest(user_list)]}')
    
"""
