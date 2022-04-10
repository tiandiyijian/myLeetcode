class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # reps = set()
        # for w in words:
        #     reps.add(''.join(codes[ord(c) - ord('a')] for c in w))
        # return len(reps)
        return len(set("".join(codes[ord(c) - ord('a')] for c in w) for w in words))
