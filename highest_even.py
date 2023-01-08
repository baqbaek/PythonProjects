def highest_even(args):
    evens = []
    for i in args:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
