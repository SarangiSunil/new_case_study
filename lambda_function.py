my_list =  [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

new_list = list(filter(lambda x: x is not None, my_list))

print(new_list)
