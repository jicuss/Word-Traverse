def flatten_array(l):
    out = []
    if isinstance(l, (list, tuple)):
        for item in l:
            out.extend(flatten_array(item))
    elif isinstance(l, (dict)):
        for dictkey in l.keys():
            out.extend(flatten_array(l[dictkey]))
    elif isinstance(l, (str, int, unicode)):
        out.append(l)
    return out