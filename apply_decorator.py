def apply_decorator(func):
    def wrapper(arg1, arg2):
        print("Decorator Applied")
        return func(arg1, arg2)
    return wrapper