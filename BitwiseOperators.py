""" 
AND(&) sets a result bit to 1 only if both corresponding bits are 1
OR(|) sets a result bit to 1 if at least one corresponding is 1
XOR(^) sets a result bit to 1 if the corresponding bits differ
NOT(~) inverts all bits (0 becomes 1, 1 becomes 0), using two's complement ~x = -(x+1)
Left Shift(<<) moves all bits left by the specified numbers of positions, filling right with zeros
Right Shift(>>) moves all bits right by the specified positions, filling left with sign bits
"""
n = 16
if n > 0 and (n & (n-1)) == 0:
    print(f'{n} is power of 2')