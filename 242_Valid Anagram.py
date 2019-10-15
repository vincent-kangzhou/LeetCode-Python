class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        alpha=[0]*26
        beta=[0]*26
        
        for i in s:
            alpha[ord(i)-97]+=1
            
        for j in t:
            beta[ord(j)-97]+=1
            
        return alpha==beta
        
        
        
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        alpha=[0]*26
        
        for i in s:
            alpha[ord(i)-97]+=1
            
        for j in t:
            alpha[ord(j)-97]-=1
            if alpha[ord(j)-97]<0:
                return False
            
        return True
        
        
        
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        alpha={}
        beta={}
        
        for i in s:
            alpha[i]=alpha.get(i,0)+1
        for j in t:
            beta[j]=beta.get(j,0)+1
        return alpha==beta
        
        
        
        
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)
