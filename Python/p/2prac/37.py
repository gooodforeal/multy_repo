def is_hashrad(x):
    return x % sum([int(el) for el in str(x)]) == 0


print(is_hashrad(13))