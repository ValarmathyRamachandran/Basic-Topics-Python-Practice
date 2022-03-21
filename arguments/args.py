def myFunction(*argv):
    for arg in argv:
        print(arg)
def kw_function(**kwargs):
    for key, value in kwargs.items():
        print((key, value))


def main():
    myFunction('hi', 'Welcome', 'to', 'args')
    kw_function(first_name ="Valarmathy", last_name = "R", id= "1")

main()
