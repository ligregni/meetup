# Word Split

import sys

class Dictionary(object):
    def __init__(self, words):
        self.s = set(words)

    def is_valid(self, word):
        return word in self.s

def word_split(string, dictionary):
    if not string:
        return 0
    dp = [0] * len(string)
    for i in xrange(len(dp)):
        for j in range(-1, i):
            if j == -1 or dp[j] != 0:
                if dictionary.is_valid(string[j+1:i+1]):
                    dp[i] = \
                        min(
                            dp[j] + 1,
                            dp[i] if dp[i] > 0 else sys.maxint) if j >= 0 \
                        else 1
    return dp[len(string)-1]
