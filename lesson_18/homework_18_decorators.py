from utils import print_separator


def log_function_args_and_results(func):
    def wrapper(*args, **kwargs):
        print_separator(50, "*")
        print(f"Calling the function '{func.__name__}' with arguments: {args}, {kwargs}")
        func_result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned result: {func_result}")
        return func_result
    return wrapper


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            print_separator(50, "*")
            print(f"Calling the function '{func.__name__}' with arguments: {args}, {kwargs}")
            func(*args, **kwargs)
        except Exception as e:
            print(f"Function '{func.__name__}' has an exception: {e}")
        return None
    return wrapper


@log_function_args_and_results
def adding(a, b):
    sum = a + b
    return sum


adding(150, 0.5)


@log_function_args_and_results
def printing_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


printing_info(name="Maryna", last_name="Doroshenko", occupation="QA")


@exception_handler
def dividing(a, b):
    return a / b


dividing(10, 0)
