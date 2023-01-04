# problem link
# https://leetcode.com/problems/bulls-and-cows/

#ideal solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Dictionary for Lookup
        lookup = Counter(secret)
        
        x, y = 0, 0
        
        # First finding numbers which are at correct position and updating x
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x+=1
                lookup[secret[i]]-=1
        
        # Finding numbers which are present in secret but not at correct position 
        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]]>0:
                y+=1
                lookup[guess[i]]-=1
        
		# The reason for using two for loop is in this problem we have 
		# to give first priority to number which are at correct position,
		# Therefore we are first updating x value
		
        return "{}A{}B".format(x, y)

#my solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        for i in [0,1,2,3,4,5,6,7,8,9]:
            dic[str(i)] = 0
        n = len(secret)
        for i in range(n):
            dic[secret[i]] += 1
        bulls = 0
        cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                dic[guess[i]] -= 1
        for i in range(n):
            if (dic[guess[i]] > 0) and (secret[i] != guess[i]):
                cows += 1
                dic[guess[i]] -= 1
        return '{}A{}B'.format(bulls,cows)

# new solution

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = []
        di = []
        n = len(secret)
        for i in range(10):
            dic.append(0)
            di.append(0)
        bulls = 0
        cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                dic[int(guess[i])] += 1
                di[int(secret[i])] += 1
        for i in range(10):
            cows += min(dic[i],di[i])
        return '{}A{}B'.format(bulls,cows)