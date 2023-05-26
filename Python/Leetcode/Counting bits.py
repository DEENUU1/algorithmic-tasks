class Solution:
    def countBits(self, n: int) -> List[int]:
        lst_num = list(range(n+1))
        
        lst_bin = []
        for i in lst_num:
            binn = bin(i).replace("0b", "")
            count = 0
            for char in binn:
                count += int(char)
            
            lst_bin.append(count)
        
        return lst_bin

            
        