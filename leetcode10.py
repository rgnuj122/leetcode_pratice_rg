class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        its = iter(s)
        itp = iter(p)
        itstmp = next(its)
        itptmp = next(itp)
solu=Solution()
print(f'{solu.isMatch("aa","a")}')