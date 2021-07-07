def f():
    city = "Munich"

    def g():
        nonlocal city
        city = "Zurich"

    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)


city = "Stuttgart"
f()
print("'city' in main: " + city)
