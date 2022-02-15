def add_until_100(array):
    if len(array) == 0:
        return 0
    chk_100 = add_until_100(array[1:])
    if array[0] + chk_100 > 100:
        return chk_100
    else:
        return array[0] + chk_100