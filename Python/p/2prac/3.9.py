def rle_encode(s):
    return [(el, s.count(el)) for el in sorted(set(s))]


print(rle_encode("ABBCCCDEF"))
