class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        dire = 0
        for _ in range(4): 
            for ins in instructions:
                if ins == "G":
                    if dire == 0:
                        y += 1
                    elif dire == 90:
                        x += 1
                    elif dire == 180:
                        y -= 1
                    elif dire == 270:
                        x -= 1
                elif ins == "L":
                    dire = (dire + 270) % 360
                elif ins == "R":
                    dire = (dire + 90) % 360
            if x == 0 and y == 0:
                return True
        
        return False