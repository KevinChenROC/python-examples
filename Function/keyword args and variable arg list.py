def f(arg1, arg2, *arg_list):
    print("arg1:", arg1)
    print("arg2:", arg2)
    for arg in arg_list:
        print("From arg_list:", arg)


f(100, 200, 300, -1, -2)
print("\n")
f(arg1=100, arg2=-1111)
