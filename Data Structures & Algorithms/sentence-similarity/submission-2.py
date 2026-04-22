class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if sentence1 == sentence2:
            return True
        if len(sentence1) != len(sentence2):
            return False
        
        similarPairsConcat = [p[0]+p[1] for p in similarPairs]
        for i in range(len(sentence1)):
            if (sentence1[i]+sentence2[i] not in similarPairsConcat) and (sentence2[i]+sentence1[i] not in similarPairsConcat) and (sentence1[i] != sentence2[i]):
                return False
            
        return True