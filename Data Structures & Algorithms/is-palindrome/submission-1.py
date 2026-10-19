class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum() == True:
                new_str+=c.lower()
        print(new_str)
        print(new_str[::-1])
        return new_str == new_str[::-1]