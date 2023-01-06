def funclist(data):
    if data == []:
        return []

    if type(data[0]) == list:
        return funclist(data[0]) + funclist(data[1:])
    else:

        return [data[0]] + funclist(data[1:])

print(funclist([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
print(funclist([1, [2, [3, [4, [5, [6, [7, [8, [9,[10]]]]]]]]]]))
print(funclist([[[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9],10]))
print(funclist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(funclist([]))

# вывод

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# []
