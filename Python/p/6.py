def main(lst):
    if 1958 in lst:
        if "OCAML" in lst:
            if "ACN.1" in lst:
                return 0
            elif "FREGE" in lst:
                if 1971 in lst:
                    return 1
                elif 2002 in lst:
                    return 2
                elif 1968 in lst:
                    return 3
        elif "X10" in lst:
            return 4
    elif 1969 in lst:
        if 1971 in lst:
            return 5
        elif 2002 in lst:
            if "OCAML" in lst:
                if "EBNF" in lst:
                    return 6
                elif "RUBY" in lst:
                    return 7
                elif "CUDA" in lst:
                    return 8
            elif "X10" in lst:
                return 9
        elif 1968 in lst:
            return 10
    elif 2016 in lst:
        return 11


def f1(lst):
    if "OCAML" in lst:
        if "ASN.1" in lst:
            return 0
        elif "FREGE" in lst:
            if 1971 in lst:
                return 1
            elif 2002 in lst:
                return 2
            elif 1968 in lst:
                return 3
    elif "X10" in lst:
        return 4


def f2(lst):
    if 1971 in lst:
        return 5
    elif 2002 in lst:
        if "OCAML" in lst:
            if "EBNF" in lst:
                return 6
            elif "RUBY" in lst:
                return 7
            elif "CUDA" in lst:
                return 8
        elif "X10" in lst:
            return 9
    elif 1968 in lst:
        return 10


def m(lst):
    if 1958 in lst:
        return f1(lst)
    elif 1969 in lst:
        return f2(lst)
    elif 2016 in lst:
        return 11


print(m([1958, 'ASN.1', 'RUBY', 1971, 'X10']))