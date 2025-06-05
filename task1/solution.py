def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, (name, expected_type) in enumerate(annotations.items()):
            if name == 'return':
                continue
            if not isinstance(args[i], expected_type):
                raise TypeError()

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(sum_two(4, 5))
