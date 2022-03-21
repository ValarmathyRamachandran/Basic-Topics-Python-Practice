#Dictionary in Python is an unordered collection
# of data values, used to store data values like a map,

def my_dict():
    Dict = {1:'Hello', 2:'Everyone', 3:'Welcome' }
    print(Dict)

    Dict = {'Name': 'python', 1: [1, 2, 3, 4]}
    print(Dict)

    Dict = dict({1:'Hello' , 2:'User' })
    print(Dict)
    print(Dict[1])
    print(Dict.get(2))

def main():
    print("Welcome to Dictionary")
    my_dict()

main()