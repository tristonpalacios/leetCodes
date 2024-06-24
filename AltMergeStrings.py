def mergeAlternately(self, word1: str, word2: str) -> str:
    # Initialize an empty list to collect characters
    merged = []
    # Iterate through the range of the maximum length of the two words
    for i in range(max(len(word1), len(word2))):
        # If the current index is within the bounds of word1, append the character from word1
        if i < len(word1):
            merged.append(word1[i])
        # If the current index is within the bounds of word2, append the character from word2
        if i < len(word2):
            merged.append(word2[i])
    # Join the list into a single string and return it
    return "".join(merged)


# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# run time 27ms beat 94.19% memory 16.36MB beat 97.59%

print(mergeAlternately("word1","abcd","pq"))
print(mergeAlternately("word1","abcd","pqr"))
print(mergeAlternately("word1","ab","pqrs"))