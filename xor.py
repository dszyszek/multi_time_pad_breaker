# first_hash = input('Input first hash \n')
# second_hash = input('Input second hash \n')

def xorF(str1, str2, amount = 166):
    str1 = str1[:amount]
    str2 = str2[:amount]

    output = ''.join(hex(int(a, 16) ^ int(b, 16))[2:] for a, b in zip(str1, str2))
    print('\n---XOR of hashes---\n')
    return print(f"\nxor of first {int(amount/2)} bytes is:\n{output}\n")

# output = xorF(first_hash, second_hash)

