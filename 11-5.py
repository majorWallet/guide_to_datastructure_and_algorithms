def unique_path(row, col):
    if row == 1 or col == 1:
        return 1
    else:
        return unique_path(row, col-1) + unique_path(row-1, col)

print(unique_path(3, 7))