class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while left <= right:
            
            #edge = spaces - ignore them
            while left < len(s) and not self.is_alpha_numeric(s[left]):
                left+=1
            while right > 0 and not self.is_alpha_numeric(s[right]):
                right-=1    

            if s[left].lower() != s[right].lower(): return False
            left+=1
            right-=1

        return True    

    def is_alpha_numeric(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))




        








"""
-logic:
1. remove all non alpha numeric ele - which are not between A-Z,a-z,0-9
-java initialize all data types
- methods
- template:
1.logic - bruteforce, sorting, - arr,tp,sl,bs,ll
2. edge case
3. dry run
 """       