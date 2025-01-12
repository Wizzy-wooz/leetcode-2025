class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    @staticmethod
    def addBinaryCarryOn(a: str, b: str) -> str:
        # Execution:
        # 1. Add leading zeroes to make both strings of equal length

        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b

        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a

        carry = '0'
        result = ''

        for i in range(len(a) - 1, -1, -1):
            # Loop over the strings from rightmost character to leftmost character

            if a[i] == '1' and b[i] == '1':
                # If both bits from 'a' and 'b' are '1':
                if carry == '1':
                    # If there's a carry ('carry' == '1'), add '1' to the result (because 1+1+1 = 11 in binary),
                    # and keep the carry as '1'.
                    result = '1' + result
                else:
                    # If there's no carry ('carry' == '0'), add '0' to the result (because 1+1 = 10 in binary),
                    # and set the carry to '1'.
                    result = '0' + result
                carry = '1'  # Update carry to '1'.

            elif a[i] == '1' or b[i] == '1':
                # If exactly one of the bits is '1' (the other is '0'):
                if carry == '1':
                    # If there's a carry ('carry' == '1'), add '0' to the result (1+0+1 = 10 or 0+1+1 = 10),
                    # and keep the carry as '1'.
                    result = '0' + result
                    carry = '1'  # Carry remains '1'.
                else:
                    # If there's no carry, add '1' to the result (1+0 = 1 or 0+1 = 1),
                    # and set the carry to '0'.
                    result = '1' + result
                    carry = '0'  # Carry is reset to '0'.

            else:
                # If both bits from 'a' and 'b' are '0':
                if carry == '1':
                    # If there's a carry ('carry' == '1'), add '1' to the result (0+0+1 = 1),
                    # and reset the carry to '0'.
                    result = '1' + result
                else:
                    # If there's no carry, add '0' to the result (0+0 = 0),
                    # and the carry remains '0'.
                    result = '0' + result
                carry = '0'  # Reset carry to '0'.

            i += 1
            # Increment 'i' at the end of the loop (though this has no functional effect
            # because the loop itself controls 'i').

        if carry == '1':
            # After processing all bits, if there's still a carry left ('carry' == '1'),
            # prepend '1' to the result.
            result = '1' + result

        return result


if __name__ == '__main__':
    print(Solution.addBinary("0010", "0111"))
    print(Solution.addBinaryCarryOn("0010", "0111"))
