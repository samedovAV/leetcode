class Solution(object):
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_length = len(haystack)
        needle_length = len(needle)

        if haystack_length < needle_length:
            return -1

        for i in range(haystack_length - needle_length):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1
