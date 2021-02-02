from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0 
        a = 0
        for i in gain:
            a += i 
            if a>height:
                height = a
        return height