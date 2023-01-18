#problem link
# https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            map = {}
            for j in points:
                if i == j:
                    continue
                dis = (i[0] - j[0])**2 + (i[1] - j[1])**2
                map[dis] = 1 + map.get(dis,0)
            for i in map:
                ans += map[i]*(map[i]-1)
        return ans