class Solution:

    def encode(self, strs:List[str]) -> str:
        res = ''
        for s in strs:  #'neet'
            res = res+str(len(s)) + '#' + s       
        return res

    # '4#neet5#codes'
    def decode(self, s: str) -> List[str]:
        #2p - l,r
        i,res = 0,[]
        while i < len(s):
            j=i  #missed
            while j < len(s):
                if s[j]!= '#':
                    j+=1   
                else:      #j == #
                    length = int(s[i:j])
                    word = s[j+1:j+1+length]
                    res.append(word)
                    i = j+1+length  #missed
                    break


        return res

        

