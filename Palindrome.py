import re
def isPalindrome(s):
    if s == "": return True
    left, right = 0, len(s) - 1
    while left < right:
        # Move left index to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right index to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        # Check if the characters are equal (ignoring case)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    # 36ms , beat 93% of answers https://leetcode.com/problems/valid-palindrome/submissions/1293577020/




