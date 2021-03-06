# An Anagram is a word or phrase that forms a different word or phrase when the letters of a word are rearranged.
# For example, the words “despair” and “praised” are anagrams

def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))
