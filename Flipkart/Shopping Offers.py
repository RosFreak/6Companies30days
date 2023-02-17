# problem link
# https://leetcode.com/problems/shopping-offers/description/

# backtracking not optimised

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        curr = 0
        for i in range(n):
            temp = [0 for _ in range(n+1)]
            temp[-1] = price[i]
            temp[i] = 1
            special.append(temp.copy())
            curr += price[i]*needs[i]
        special = list(filter(lambda s: all(s[i] <= needs[i] for i in range(len(needs))), special))
        currneeds = [0 for _ in range(n)]
        def solve(currneeds,curr,mincurr):
            # print(currneeds,curr)
            if currneeds == needs:
                mincurr = min(curr,mincurr)
                return mincurr
            for i in range(n):
                if currneeds[i] > needs[i]:
                    return mincurr
            for x in range(len(special)):
                curr += special[x][-1]
                if curr > mincurr:
                    curr -= special[x][-1]
                    continue 
                for k in range(n):
                    currneeds[k] += special[x][k]
                mincurr = solve(currneeds,curr,mincurr)
                curr -= special[x][-1]
                for k in range(n):
                    currneeds[k] -= special[x][k]
            return mincurr
            
        return solve(currneeds,0,curr)

# DFS + memoization
# TLE at last case

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        d = {}
        special = list(filter(lambda s: all(s[i] <= needs[i] for i in range(len(needs))), special))
        def dfs(cur):
            val = sum(cur[i]*price[i] for i in range(len(needs))) #cost without special
            for spec in special:
                if spec[-1]  > val:
                    continue
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0: # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1]) # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val
        return dfs(needs)