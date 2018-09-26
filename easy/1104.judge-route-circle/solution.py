class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        if len(moves)<2:
            return False
        if moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R"):
            return True
        return False