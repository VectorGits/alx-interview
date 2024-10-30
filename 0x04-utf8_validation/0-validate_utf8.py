#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    method that determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0

    for num in data:
        binary_rep = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in binary_rep:
                if bit == '0':
                    break
                num_bytes += 1
                    
                if num_bytes == 0:
                    continue

                if num_bytes == 1 or num_bytes > 4:
                    return False

            else:
                if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                    return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [
        80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33
        ]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
