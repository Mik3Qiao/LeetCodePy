# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         length = len(s)
#         longest = 0
#         dict = {}
#
#         counter = 0
#         for i in range(length):
#             if s[i] in dict:
#                 counter = max(dict[s[i]], counter)
#
#             longest = max(longest, i - counter + 1)
#             dict[s[i]] = i + 1
#
#         return longest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list
