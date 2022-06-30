def create_counter():
    i = 0
    
    def func():
        nonlocal i
        i += 1
        return i
    
    return func


counter = create_counter()