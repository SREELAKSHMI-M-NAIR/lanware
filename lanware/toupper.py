def uppercase(fun):

    def wrapper():

        res = fun()
        decorator = res.upper()

        return decorator
    return wrapper

@uppercase
def toupper():
    return 'sree'

msg = toupper()
print(msg)