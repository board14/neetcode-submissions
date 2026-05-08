class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ss={}
        hs={}
        for i in range(len(s)):
            ss[s[i]]=1+ss.get(s[i],0)
            hs[t[i]]=1+hs.get(t[i],0)

        for i in ss:
            if ss[i]!=hs.get(i,0):
                return False

            

        



            
        return True