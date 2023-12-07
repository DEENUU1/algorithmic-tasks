class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitue = 0

        for g in gain:
            altitude += g
            max_altitue = max(max_altitue, altitude)

        return max_altitue