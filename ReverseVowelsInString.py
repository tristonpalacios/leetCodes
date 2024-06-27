def reverseVowels( s: str) -> str:
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    s_list = list(s)
    l, r = 0, len(s_list) - 1

    while l < r:
        if s_list[l] not in vowels:
            l += 1
        elif s_list[r] not in vowels:
            r -= 1
        else:
            # Use tuple unpacking for efficient swapping
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

    return ''.join(s_list)

print(reverseVowels("leetcode"))