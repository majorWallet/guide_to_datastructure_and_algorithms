def golomb(n, memo):
    if n == 1:
        return 1
    else:
        if not memo.get(n):
            memo[n] = 1 + n - golomb(golomb(n-1, memo), memo)
        return memo[n]