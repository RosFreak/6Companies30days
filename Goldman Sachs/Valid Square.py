#problem link
# https://leetcode.com/problems/valid-square/description/

def distance(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        s = set()
        s.add(distance(p1,p2))
        s.add(distance(p1,p3))
        s.add(distance(p1,p4))
        s.add(distance(p2,p3))
        s.add(distance(p2,p4))
        s.add(distance(p3,p4))
        if len(s)==2 and (0 not in s):
            return True
        return False