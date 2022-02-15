def found_x(str, i = 0):
    if str[0] == 'x':
        return i
    else:
        return found_x(str[1:], i + 1)

print(found_x("abcdefghijklmnopqrstuvwxyz"))