class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    @staticmethod
    def addBinaryCarryOn(a: str, b: str) -> str:
        # Pad both strings to the same length
        a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))

        carry = 0
        result = []

        # Traverse both strings from the rightmost bit to the leftmost
        for i in range(len(a) - 1, -1, -1):
            # Convert characters to integers and calculate sum + carry
            bit_a, bit_b = int(a[i]), int(b[i])
            total = bit_a + bit_b + carry

            # Compute the new bit (total % 2) and the carry (total // 2)
            result.append(str(total % 2))
            carry = total // 2

        # If there's a carry left after the loop, prepend it
        if carry:
            result.append('1')

        # Reverse the result and join it into a string
        return ''.join(reversed(result))


if __name__ == '__main__':
    print(Solution.addBinary("0010", "0111"))
    print(Solution.addBinaryCarryOn("0010", "0111"))
