class Solution:
    def findPermutation(self, s):
        def gen(s, path=''):
            if not s:
                yield path

            for i in range(len(s)):
                yield from gen(s[:i] + s[i + 1:], path + s[i])

        res = set(gen(s))
        return list(res)