def multiply():
    result = 10.5 * 4
    return result


print(multiply())


def multiply(x, y):
    result = x * y
    return result


print(multiply(10.5, 4))


def add(x, y):
    try:
        if x < 5:
            raise ValueError("X cannot be lower than 5")
        return x + y
    except ValueError:
        return None

print(add(3, 5))
