def f(*arg_list, arg1, arg2):
    print("arg1:", arg1)
    print("arg2:", arg2)
    for arg in arg_list:
        print("From arg_list:", arg)


# f(100, 200, 300, -1, -2) # this produce errors because keyword args are not specified.
print("\n")
f(1, 2, 3, arg1=100, arg2=-1111)
