

def decorator(func):

    def wrapper(a,b,c,d):
        print("this is wrapper funtion",a,b,c,d)
        return func(a,b)
    return wrapper

@decorator
def add(a,b):
    print("this is A method")
    return a+b


b=add(4,5, 7, 8)
print(b)
