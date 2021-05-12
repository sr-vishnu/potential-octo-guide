def read_text_file(path):
    with open(path,'r') as fp:
        lines = fp.readlines()
        lines = list(map(lambda x:x.strip("\n"),lines))
    return list(lines)