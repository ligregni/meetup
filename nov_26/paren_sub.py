def longest_paren(s):
    if len(s) == 0:
        return 0
    dp = [0] * len(s)
    for i,x in enumerate(s):
        if x == ')':
            if i > 0:
                prev = -1
                if s[i-1] == '(':
                    dp[i] = 2
                    if i > 1:
                        prev = i-2
                else:
                    prev = dp[i-1]
                    if i-prev > 0 and s[i-prev-1] == '(':
                        dp[i] = prev+2
                        prev = i-dp[i-1]-1
                    else:
                        prev = -1
                if prev != -1:
                    dp[i] += dp[prev]
    return max(dp)
