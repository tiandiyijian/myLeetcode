class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = set('aeiou')
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            if word[0].lower() in vowel:
                word += 'ma' + 'a'*(i+1)
            else:
                word = word[1:] + word[0] + 'ma' + 'a'*(i+1)
            sentence[i] = word
        return ' '.join(sentence)