class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        store = {}
        for i in s:
            if i in store:
                store[i] +=1
            else:
                store[i] = 1
        for i in t:
            if i not in store:
                return False
            if i in store:
                store[i] -=1
                if store[i] < 0:
                    return False
        return True