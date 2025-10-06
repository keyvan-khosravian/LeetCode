class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_letters = {}

        for c in magazine:
            if not c in magazine_letters:
                magazine_letters[c] = 1
            else:
                magazine_letters[c] += 1
        
        for r in ransomNote:
            if not r in magazine_letters:
                return False

            if magazine_letters[r] == 1:
                del magazine_letters[r]
            else:
                magazine_letters[r] = magazine_letters[r] - 1
        
        return True