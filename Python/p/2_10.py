def f(s, c):
    count = 0
    for char in s:
        if char.lower() == c.lower():
            count += 1
    return count


def count_characters(s):
    res = {}
    for char in s:
        if char == " ":
            continue
        char = char.lower()
        res[char] = f(s, char)
    return res


print(count_characters("I love the Python programming language!"))
