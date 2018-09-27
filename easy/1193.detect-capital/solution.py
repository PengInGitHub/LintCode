class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse1(self, word):
        # write your code here
        uppers = [l for l in word if l.isupper()]
        if len(uppers) == 0 or len(uppers)==len(word):
            return True
        elif len(uppers) == 1 and word[0] in uppers:
            return True
        return False
            
    #string processing
    def detectCapitalUse2(self, word):
        return word.isupper() or word.islower() or word.istitle()
    
    # regular expression
    def detectCapitalUse(self, word):
        import re
        pat = '([A-Z]*|[A-Z][a-z]*|[a-z]*)$'
        return True if re.compile(pat).match(word) else False
