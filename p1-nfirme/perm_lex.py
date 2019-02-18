def perm_gen_lex(a):

    if len(a) == 0:  # if string has length of 0 return empty list
        return []
    elif len(a) == 1:  # if string has length of 1 return list with single value
        return [a]
    else:
        list = []
        for i in range(len(a)):  # iterates through all characters in input string
            c = a[i]  # single character from input string
            simple = a[:i] + a[i + 1:]  # creates the simpler string by removing single character
            for p in perm_gen_lex(simple):
                list.append(c + p)
        return list



