from typing import List


class Solution:
    @staticmethod
    def findThePrefixCommonArray(array_a: List[int], array_b: List[int]) -> List[int]:
        ans = []
        vis = [1] * (len(array_a) + 1)
        s = 0
        for a, b in zip(array_a, array_b):
            vis[a] ^= 1
            s += vis[a]
            vis[b] ^= 1
            s += vis[b]
            ans.append(s)
        return ans


if __name__ == '__main__':
    print(Solution.findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))
