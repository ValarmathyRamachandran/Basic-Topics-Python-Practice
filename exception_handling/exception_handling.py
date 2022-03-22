def my_function(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    my_function(3)
    my_function(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


def finally_function():
    # Python program to demonstrate finally

    # No exception Exception raised in try block
    try:
        k = 5 // 0  # raises divide by zero exception.
        print(k)

    # handles zerodivision exception
    except ZeroDivisionError:
        print("Can't divide by zero")

    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')


if __name__ == "__main__":
    finally_function()
