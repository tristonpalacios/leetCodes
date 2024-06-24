from math import gcd
def gcdOfStrings(self, str1: str, str2: str) -> str:
    # Check if concatenated strings are equal or not, if not return ""
    if str1 + str2 != str2 + str1:
        return ""
    # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)

    return str1[:gcd(len(str1), len(str2))]

gcdOfStrings("","ababab","abab")