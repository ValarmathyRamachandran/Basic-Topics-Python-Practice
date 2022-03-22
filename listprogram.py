def list_function():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(str(list1))
    print(str(list2))
    result_list = []
    for x in range(0, len(list1)):
        result_list.append(list1[x] + list2[x])
    print(str(result_list))

list_function()
