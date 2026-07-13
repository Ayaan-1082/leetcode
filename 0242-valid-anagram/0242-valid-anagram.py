class Solution(object):
    def isAnagram(self, s, t):
        # if len(s) != len(t) :
        #     return False
        # d1 = {}
        # for a in s:
        #     if a not in d1.keys():
        #         d1[a] = 1
        #     else :
        #         d1[a] = d1[a] + 1
        # for a in t:
        #     if a not in d1.keys():
        #         return False
        #     else :
        #         d1[a] = d1[a] - 1
        # for k in d1.values():
        #     if k!=0:
        #         return False

        # return True
        return sorted(s)==sorted(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        