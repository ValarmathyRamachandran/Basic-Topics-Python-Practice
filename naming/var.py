def var_function():
    myvar = "John" #variable name must start with a letter or the underscore character
    #2var = "Hi"   A variable name cannot start with a number
    my_var = "John" #A variable name can only contain alpha-numeric characters and underscores
    _my_var = "John"
    myVar = "John"
    MYVAR = "John" #Variable names are case-sensitive (age, Age and AGE are three different variables)
    myvar2 = "John"

    print(myVar, my_var, myvar2, MYVAR, myvar)

def main():
    var_function()

main()