class Solution:
    def isPalindrome(self, s: str) -> bool:
        #set it up
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str+=c.lower()
                
        #2 pointers
        l = 0
        r = len(new_str) - 1

        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l +=1
            r -=1

        return True


