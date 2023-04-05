def f(lst):
    res = ""
    for i in range(len(lst) - 1, -1, -1):
        if i == 0:
            res += lst[i]
        else:
            res += lst[i] + " "
    return res


print(f(["language!", "programming", "Python", "the", "love", "I"]))
