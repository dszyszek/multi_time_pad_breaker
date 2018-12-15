from find_letters import main
from xor import xorF

hash_to_break = input('Input XOR to break (hex):\n')


def breaker(hash):
    sec = []
    possible_message = []


    for i, x in enumerate(hash):        # divide hash intp byte fractions
        if not i % 2 == 0:
            sec.append(hash[i-1] + hash[i])
    print(sec, 'sec')

    for i, byte in enumerate(sec):
        if not byte == '00' and int(byte, 16) <= 128:
            pairs = main(byte)

            if len(pairs) == 2:
                pairs.pop()
                for single_pair in pairs:
                    single_pair.sort()
                    single_pair.reverse()

                    possible_message.append(single_pair[0])
            else:
                possible_message.append(str(i + 1))

        else:
            possible_message.append(str(i + 1))

    message = '|'.join(possible_message)
    return message


broken_message = breaker(hash_to_break)

print("\n====================================")
print("Broken message")
print("====================================\n")
print(broken_message, 'broken_message')