class Solution(object):
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}
        for a in s:
            if a not in d1.keys():
                d1[a] = 1
            else :
                d1[a] = d1[a] + 1
        for a in t:
            if a not in d2.keys():
                d2[a] = 1
            else :
                d2[a] = d2[a] + 1

        return d1==d2
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        