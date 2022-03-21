#Set is an unordered collection of data type that is iterable, mutable and
# has no duplicate elements

def set_function():
    #creating a set
    set1 = set("Welcome to data types")
    print(set1)

    set2 = set(["hello", "everyone"])
    print(set2)

    set3 = set([1,2,"hi",3,"Good Morning"])
    print(set3)

    # Accessing element using
    # for loop
    print("\nElements of set: ")
    for i in set2:
        print(i, end=" ")

def main():
    print("Hello from main")
    set_function()

main()