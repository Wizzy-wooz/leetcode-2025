class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        # Define a function to add two binary strings 'a' and 'b', returning their binary sum as a string.

        if len(a) > len(b):
            # If the length of 'a' is greater than 'b', pad 'b' with leading zeros
            # so that both strings are of equal length.
            b = '0' * (len(a) - len(b)) + b

        if len(a) < len(b):
            # If the length of 'b' is greater than 'a', pad 'a' with leading zeros
            # so that both strings are of equal length.
            a = '0' * (len(b) - len(a)) + a

        c, i = '0', 0
        # Initialize the carry ('c') to '0' since there is no carry at the start.
        # Initialize a variable 'i' (though it's later reassigned in the loop).

        result = ''
        # Initialize an empty string 'result' to build the final binary sum.

        for i in range(len(a) - 1, -1, -1):
            # Loop over the strings from the least significant bit (rightmost character)
            # to the most significant bit (leftmost character).

            if a[i] == '1' and b[i] == '1':
                # If both bits from 'a' and 'b' are '1':
                if c == '1':
                    # If there's a carry ('c' == '1'), add '1' to the result (because 1+1+1 = 11 in binary),
                    # and keep the carry as '1'.
                    result = '1' + result
                else:
                    # If there's no carry ('c' == '0'), add '0' to the result (because 1+1 = 10 in binary),
                    # and set the carry to '1'.
                    result = '0' + result
                c = '1'  # Update carry to '1'.

            elif a[i] == '1' or b[i] == '1':
                # If exactly one of the bits is '1' (the other is '0'):
                if c == '1':
                    # If there's a carry ('c' == '1'), add '0' to the result (1+0+1 = 10 or 0+1+1 = 10),
                    # and keep the carry as '1'.
                    result = '0' + result
                    c = '1'  # Carry remains '1'.
                else:
                    # If there's no carry, add '1' to the result (1+0 = 1 or 0+1 = 1),
                    # and set the carry to '0'.
                    result = '1' + result
                    c = '0'  # Carry is reset to '0'.

            else:
                # If both bits from 'a' and 'b' are '0':
                if c == '1':
                    # If there's a carry ('c' == '1'), add '1' to the result (0+0+1 = 1),
                    # and reset the carry to '0'.
                    result = '1' + result
                else:
                    # If there's no carry, add '0' to the result (0+0 = 0),
                    # and the carry remains '0'.
                    result = '0' + result
                c = '0'  # Reset carry to '0'.

            i += 1
            # Increment 'i' at the end of the loop (though this has no functional effect
            # because the loop itself controls 'i').

        if c == '1':
            # After processing all bits, if there's still a carry left ('c' == '1'),
            # prepend '1' to the result.
            result = '1' + result

        return result
        # Return the final binary sum as a string.


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("0010", "0111"))
