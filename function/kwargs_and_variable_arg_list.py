def f(arg1, arg2, *arg_list, **kwargs ):
    print("pos_arg1:", arg1)
    print("pos_arg2:", arg2)
    
    print("======From *arg_list=======")
    for arg in arg_list:
        print("From arg_list:", arg)
        
    print("======From **kwargs=======")
    for key,value in kwargs.items():
        print ("(%s, %s)" %(key, value))


f("hello","world", 5,5,5,5,5, first="Geeks",mid="for",last="Geeks" )