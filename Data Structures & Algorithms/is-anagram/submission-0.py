class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ss={}
        hs={}
        for i in range(len(s)):
            if s[i] in ss:
                ss[s[i]]+=1
            else:
                ss[s[i]]=1
            if t[i] in hs:
                hs[t[i]]+=1
            else:
                hs[t[i]]=1
        print(hs)
        print(ss)
        for i in range (len(s)):
            if s[i] in hs:
                print(ss[s[i]])
                print(hs[s[i]])
                if ss[s[i]]!=hs[s[i]]:
                    return False
                
            else:
                return False
               
        



            
        return True