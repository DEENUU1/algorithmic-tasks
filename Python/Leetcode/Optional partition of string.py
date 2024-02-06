class Solution:
    def partitionString(self, s: str) -> int:
        
        res = []
        tmp = []  

        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.append(s[i])
            else:
                res.append(tmp)
                tmp = [s[i]]  
        if tmp:  
            res.append(tmp)
            
        return len(res)
