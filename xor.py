first_hash = input('Input first hash \n')
second_hash = input('Input second hash \n')

def xorF(str1, str2, amount = 166):
    str1 = str1[:amount]
    str2 = str2[:amount]

    output = ''.join(hex(int(a, 16) ^ int(b, 16))[2:] for a, b in zip(str1, str2))
    print('\n---XOR of hashes---\n')
    return print(f"\nxor of first {int(amount/2)} bytes is:\n{output}\n")

output = xorF(first_hash, second_hash)


# pyQT5 -> GUI Python lib
# Key: 66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a61
