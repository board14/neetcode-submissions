class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        j = n - 1
        i = 0
        
        # # Changed to .isalnum() to properly handle single characters/numbers
        # if s == " " or (n == 1 and (not s[0].isalnum())):
        #     return True
            
        while i < j:           
            # Changed to .isalnum() so it stops on numbers instead of skipping them
            while i < j and not s[i].isalnum():
                i += 1 
                
            # Changed to .isalnum() here as well
            while i < j and not s[j].isalnum():
                j -= 1
            
            if i < j and s[j].lower() != s[i].lower():
                return False
                
            j -= 1
            i += 1
            
        return True