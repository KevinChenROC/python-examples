def test_decorator(func, msg="Test 123"):
    def wrapper(*args, **kwargs):
        print("Msg: " + msg)
        func(*args, **kwargs)
        
    return wrapper


@test_decorator
def say_hello(name):
    print("Hello, "+name)
    

say_hello("Kevin")