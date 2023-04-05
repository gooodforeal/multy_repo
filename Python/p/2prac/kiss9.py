def main(tbl):
    for line in tbl:
        line = [val for val in line if val]
        for i in range(len(line)):
            if line[i].count("-") == 2:
                bf = line[i].split("-")
                tf2 = bf[2][2::]
                tf1 = bf[2][0:2:]
                line[i] = f"({bf[0]}) {bf[1]}-{tf1}-{tf2}"
    return [tbl[j][i] for j in range(len(tbl)) for i in range(len(tbl[0]))]


print([[None, "03/01/01", "true", None, "537-825-9476"], [None, "03/05/00", "false", None, "738-552-9820"]])
