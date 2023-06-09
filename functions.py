def multiply():
    result = 10.5 * 4
    return result


print(multiply())


def multiply(x, y):
    result = x * y
    return result


print(multiply(10.5, 4))


def add(x: int = 5, y: int = 5) -> int:
    try:
        if x < 5:
            raise ValueError("X cannot be lower than 5")
        return x + y
    except ValueError as valueError:
        print(str(valueError))
        return None
    except TypeError as typeError:
        print(str(typeError))
        return None


print(add())

print("--------")


def func(p1, p2, *args, k, **kwargs):
    print("p1 {0} and p2 {1}".format(p1, p2))
    print("*args {}".format(args))
    print("k {}".format(k))
    print("**kwargs {}".format(kwargs))


func(1, 2, 3, 4, 5, k=1, k1=2, k2=3, k3=4)
