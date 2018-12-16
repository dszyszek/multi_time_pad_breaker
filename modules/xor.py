def xorF(str1, str2, amount = 166):
    str1 = str1[:amount]
    str2 = str2[:amount]

    output = ''.join(hex(int(a, 16) ^ int(b, 16))[2:] for a, b in zip(str1, str2))
    print('\n---XOR of hashes---\n')
    return output

# output = xorF(first_hash, second_hash)

