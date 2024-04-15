def example_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


@example_decorator
def function_with_args(a, b):
    return a + b


@example_decorator
def function_with_kwargs(x=0, y=0):
    return x * y


@example_decorator
def function_with_args_and_kwargs(a, b, x=0, y=0):
    return a + b + x * y


res1 = function_with_args(3, 5)
print(res1)
function_with_kwargs(x=2, y=3)
function_with_args_and_kwargs(1, 2, x=4, y=5)
