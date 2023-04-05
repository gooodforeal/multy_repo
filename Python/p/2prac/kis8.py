def main(s):
    s = s.replace("\n", "")
    buff = s.split("=:")
    titles = []
    values = []
    res = {}
    for i in range(1, len(buff)):
        bf = buff[i].split(".")[0].strip()
        bf = bf.replace("'", "")
        titles.append(bf)
    buff2 = s.split("declare")
    buff2 = [el for el in buff2 if "list" in el]
    buff2 = [el.split("=:")[0].strip() for el in buff2]
    for i in range(len(buff2)):
        buff2[i] = buff2[i].replace("list", "")
        buff2[i] = buff2[i].replace("@", "")
        buff2[i] = buff2[i].replace(" ", "")
        buff2[i] = buff2[i].replace(")", "")
        buff2[i] = buff2[i].replace("(", "")
        buff2[i] = buff2[i].replace("'", "")
        values.append(buff2[i].split(","))
    for i in range(len(titles)):
        res[titles[i]] = values[i]
    return res



print(main(".begin begin declare list(@'ceza' , @'bige',@'edrien' , @'gebe' ) =:'geon'. end; begin declare list( @'oratxe',@'dimaat' , @'onis_495',@'oran' ) =:'esaxeat_923'. end;begin declare list(@'edxear_952' ,@'diqu_936' , @'tien_79' )=: 'aaana_863'. end;begin declare list(@'arce' , @'beorti_983', @'celate_16' , @'arve' ) =:'qugeso'. end;.end"))