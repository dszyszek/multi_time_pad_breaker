from find_letters import main
from xor import xorF

hash_to_break = input('Input XOR to break (hex):\n')


def breaker(hash):
    print('\n-----------------Computing-----------------\n')
    sec = []
    possible_message = []

    for i, x in enumerate(hash):        # divide hash into byte fractions
        if not i % 2 == 0:
            sec.append(hash[i-1] + hash[i])

    while len(possible_message) < len(hash_to_break)/2:
        for i, byte in enumerate(sec):
            pairs = main(byte)

            if len(pairs) == 1 and not byte == '00' and int(byte, 16) <= 128:
                sorted = [pairs[0].pop(pairs[0].index(x)) for x in pairs[0] if not x == ' ']  # pop() every ' ' in 'pairs'

                possible_message.append(sorted[0])
            else:
                possible_message.append(str(i+1))

    message = ' - '.join(possible_message)
    return message


broken_message = breaker(hash_to_break)

print("\n====================================")
print("Broken message")
print("====================================\n")
print(broken_message, 'broken_message')