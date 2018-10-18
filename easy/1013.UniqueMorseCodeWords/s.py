class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        morses = []
        # Write your code here
        for word in words:
            morse = self.getMorse(word)
            morses.append(morse)
        print (morses)
        return len(set(morses))
            
    def getMorse(self, word):
        res = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        for char in word:
            print(char)
            print(morse[alpha.index(char)])
            res.append(morse[alpha.index(char)])
        return ''.join(res)
            