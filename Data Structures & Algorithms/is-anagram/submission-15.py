class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        store = {}
        for c in s:
            if c not in store:
                store[c] = 1
            else:
                store[c] +=1
            
        for c in t:
            if c not in store:
                return False
            else:
                store[c] -=1
            
            if store[c] == 0:
                del(store[c])

        return not store
        