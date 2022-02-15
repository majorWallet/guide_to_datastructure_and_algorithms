def unique_paths(row, col, memo):
    if row == 1 or col == 1:
        return 1
    else:
        if not memo[row][col]:
            memo[row][col] = unique_paths(row-1, col, memo) + unique_paths(row, col-1, memo)
        return memo[row][col]