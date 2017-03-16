from functools import wraps

#
# func = debug(func)
#
def debug(func):
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugprefix(prefix=''):
    def debug(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return debug

def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

# metaclass because it is a subclass of type
class DebugClass(type):
    def __new__(meta, clsname, bases, clsdict):
        cls = super().__new__(meta, clsname, bases, clsdict)
        return debugmethods(cls)
