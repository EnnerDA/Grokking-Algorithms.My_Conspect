def find_smallest(user_list):
    smallest = user_list[0]
    smallest_index = 0
    for i in range(len(user_list)):
        if user_list[i] < smallest:
            smallest = user_list[i]
            smallest_index = i
    return smallest_index
