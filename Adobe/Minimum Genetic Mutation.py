# problem link
# https://leetcode.com/problems/minimum-genetic-mutation/description/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = [startGene]
        visited = defaultdict(int)
        for b in bank:
            visited[b] = 1
        steps = 0
        n = len(startGene)
        while len(queue) > 0:
            size = len(queue)
            while(size):
                curr = queue.pop(0)
                if curr == endGene:
                    return steps
                for a in ['A','C','G','T']:
                    for i in range(n):
                        cpy = curr
                        cpy = cpy[:i] + a + cpy[i+1:]
                        # print(v)
                        if ( visited[cpy] == 1) :
                            queue.append(cpy)
                            visited[cpy] = 2
                size -= 1
            steps += 1
        return -1