from find_smallest import find_smallest

def selection_sort(user_list):
    new_user_list = []
    for i in range(len(user_list)):
        smallest_index = find_smallest(user_list)
        new_user_list.append(user_list.pop(smallest_index))
    return new_user_list
    
"""
#TEST function

from random import randint
user_list = []
for x in range(0, 11):
    user_list.append(randint(1,100))
print(f'изначальный список: \n\t{user_list}')
print(f'отсортированный список: \n\t{selection_sort(user_list)}')
"""   
