class Solution:

    def encode(self, strs: List[str]) -> str:
        #4#neet4#code4#love3you
        res = ""
        for s in strs:
            res = res + str(len(s))+ "#" + s
        return res    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # extract number before #
            word = s[j+1 : j+1+length]  # extract the word
            res.append(word)
            i = j + 1 + length  # move to the start of next encoded part

        return res

      





"""
- just having length - will break when len is 2 digits 
ex: 4neet4code - if word is more than 10 breaks 
- hence use delimiter    

- in decode use while loop as we are jumping in diff steps
"""