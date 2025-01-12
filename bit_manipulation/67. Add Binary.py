class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        # [2:] remove 0b
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    print(Solution.addBinary("0010", "0111"))
