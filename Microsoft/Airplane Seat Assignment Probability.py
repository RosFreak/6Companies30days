# problem link
# https://leetcode.com/problems/airplane-seat-assignment-probability/description/

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n==1:
            return 1.0
        return 0.50