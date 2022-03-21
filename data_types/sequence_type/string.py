"""
The string can be defined as the sequence of characters represented in the quotation marks. In Python, we can use single,
double, or triple quotes to define a string.

"""
def main():
    ''' s docstrings'''
    str = "string using double quotes from main fn"
    print(str)
    s = '''A multiline 
    string from main '''

    print(s)

def seq():
    str1 = 'hello everyone' #string str1
    str2 = ' how are you' #string str2
    print (str1[0:2]) #printing first two character using slice operator
    print (str1[4]) #printing 4th character of the string
    print (str1*2) #printing the string twice
    print (str1 + str2) #printing the concatenation of str1 and str2

seq()
main()