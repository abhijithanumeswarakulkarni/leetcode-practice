class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        hmap = {}
        for pair in similarPairs:
            word1, word2 = pair
            if word1 in hmap:
                hmap[word1].append(word2)
            else:
                hmap[word1] = [word2]
            
            if word2 in hmap:
                hmap[word2].append(word1)
            else:
                hmap[word2] = [word1]
        
        m, n = len(sentence1), len(sentence2)
        if m != n:
            return False
        
        for i in range(m):
            word1, word2 = sentence1[i], sentence2[i]
            if word1 == word2:
                continue

            if word1 not in hmap or word2 not in hmap:
                return False
            
            if (word1 in hmap and word2 not in hmap[word1]) or (word2 in hmap and word1 not in hmap[word2]):
                return False
        
        return True