class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter(str.isalnum, '~`!@#$%^&*()1234567890_+[]{\}|:";<>?,./')
        s = ''.join(filter(str.isalnum, s)).lower()
        news= s[::-1]
        return True if s == news else False