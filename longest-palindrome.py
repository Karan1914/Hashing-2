class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        let = {}
        
        for i in s:
            if i not in let:
                let[i] = 1
            else:
                let[i]+=1
                
        res = 0
        odd = 0
        
        if len(let)==1:
            return let[s[o]]
        
        for i in let.values():
            if i>1:
                if i%2==0:
                   res+=i
                else:
                   res += i-1
                   odd += 1
            else:
                odd+=1
                   
        if odd>0:
            res+=1
        return res
                   
                   
                
        
            
        