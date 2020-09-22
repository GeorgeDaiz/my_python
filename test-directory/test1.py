class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        if not s:
            return ''

        def spread_from_center(string, center, offset):
            left = center
            right = center + offset
            count = len(string)
            while left >= 0 and right < count and string[left] == string[right]:
                left -= 1
                right += 1
            left = left + 1
            res = string[left: right]
            return res

        max_str = ''
        for i in range(len(s)):
            res1 = spread_from_center(s, i, 0)
            res2 = spread_from_center(s, i, 1)
            if len(res1) > len(max_str):
                max_str = res1
            if len(res2) > len(max_str):
                max_str = res2

        return max_str
