from collections import Counter


class Solution:
    @staticmethod
    def minimumLength(s: str) -> int:
        cnt = Counter(s)
        return sum(1 if x & 1 else 2 for x in cnt.values())


if __name__ == '__main__':
    print(Solution.minimumLength('abaacbcbb'))
