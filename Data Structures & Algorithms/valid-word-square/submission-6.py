class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            column = ''
            for j in range(len(words)):
                try:
                    column += words[j][i]
                except:
                    break
            if column != words[i]:
                return False
        return True

'''
b a l l
a s e e
l e t
l e p

'''