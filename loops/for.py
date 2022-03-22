# Python program to illustrate
# Iterating over a list
def list_fn():
    print("List Iteration")
    l = ["Welcome", "to", "Python"]
    for i in l:
        print(i)
    return l

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("welcome", "to ", "python")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "python"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),


if __name__ == "__main__":
    list_fn()
