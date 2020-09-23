from functools import wraps


def set_n_positional_args(n):
    def decorator(func):
        @wraps(func)  # to preserve function name
        def wrapper(*args, **kwargs):
            assert len(args) >= n, \
                f"{func.__name__} takes {n} position arguments but {len(args)} was given"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@set_n_positional_args(2)
def sum_3_numbers(a, b, c):
    return a + b + c


print(sum_3_numbers(1, 2, 3))
print(sum_3_numbers(1, 2, c=3))
print(sum_3_numbers(1, b=2, c=3))
