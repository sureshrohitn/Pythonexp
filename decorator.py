def name_decorator(name):
    def wrapper(arg1):
        arg1=arg1.capitalize()
        return arg1
    return wrapper

@name_decorator
def hello1(name):
    return name
hello1('suresh')
