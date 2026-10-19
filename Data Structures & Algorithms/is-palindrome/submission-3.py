class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str+=c.lower()
        
        reverse_str = (new_str[::-1])
        if (new_str == reverse_str):
            return True
        else:
            return False