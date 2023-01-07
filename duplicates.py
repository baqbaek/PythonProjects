my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for i in my_list:
    if my_list.count(i) > 1:
        duplicates.append(i)
print(duplicates)
