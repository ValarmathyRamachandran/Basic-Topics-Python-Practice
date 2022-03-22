#Lists are used to store multiple items in a single variable.
def list_function():
    list1 = [1, 5, 7, 9, 3]
    list2 = [True, False, False]
    list3 = ["mike", 34, True, 40, "male", 88]
    list2[1] = True   #change item value in list
    list1.insert(2, "4") #insert() method inserts an item at the specified index
    print(list1, list2)
    print(list3)
    print(list3[2:5])
    list1.append(10) #To add an item to the end of the list, use the append() method
    #print(list1)
    return list1

"""def main():
   my_list = ["java", "html", "css", "javascript", "react"]
    print(my_list)

    list_constructor = list(("name", "id", "phone number"))
    print(list_constructor)
    print(list_constructor[-1]) # refers to the last item
    list_constructor.pop() #removes the last item.
    list_constructor.pop(1) #removes the second item.
    list_constructor.remove("name")
    print(list_constructor)"""


if __name__ == "__main__":
    list_function()
