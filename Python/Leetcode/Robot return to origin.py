class Solution:
    def judgeCircle(self, moves: str) -> bool:
        upDown = 0
        leftRight = 0

        for char in moves:
            if char == "U":
                upDown += 1
            elif char == "D":
                upDown -= 1
            elif char == "L":
                leftRight += 1
            elif char == "R":
                leftRight -= 1
            
        if upDown == 0 and leftRight == 0:
            return True
        return False