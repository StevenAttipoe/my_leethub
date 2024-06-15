class Solution:
    def isValid(self, word: str) -> bool:
        if (len(word) < 3):
            return False

        vowels = {'a', 'e', 'i', 'o', 'u'}
        hasVowel = hasConsonant = False
        hasDigit = hasEnglishLetters = False

        for char in word:
            if (char.lower() in vowels):
                hasVowel = True

            if (char.isdigit()):
                hasDigit = True

            elif (char.isalpha()):
                hasEnglishLetters = True

                if (char.lower() not in vowels):
                    hasConsonant = True

            else:
                return False

        return hasVowel and hasConsonant and (hasDigit or hasEnglishLetters)




        