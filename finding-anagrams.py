# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

__first = input("Enter the first word: ")
__second = input("Enter another word to check: ")

print("Anagram is: ", find_anagram(__first, __second))
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
