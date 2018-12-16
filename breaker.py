from modules.find_letters import find_letters
from modules.xor import xorF
from pyfiglet import figlet_format
from termcolor import colored

print("\n=================================================================")

header = colored(figlet_format('MTP BREAKER'), color='magenta')
print(header)

print("=================================================================\n")

print('If you want to break stream cipher, that uses OTP many times, you have to input ciphertexts of two messages, that are encrypted using same key. ')
print('The program will try to find each letter from given ciphertexts, so output will look like: ')
print('e - x - a - 4 - p - 6 - e')
print('If program cannot find any letters matching to given hex value, or there are too many letters matching that, ')
print('program will output number that indicates position of that letter in decrypted message.')
print('Remember! The more hashes you input, the greater chance you have to decrypt the message!')

print("\n=================================================================\n")


first_hash = input('Input ciphertext of first message: \n')
second_hash = input('\nInput second hash: \n')

hash_to_break = xorF(first_hash, second_hash)
print(hash_to_break)

def breaker(hash):
    print('\n---------------------------Computing---------------------------\n')

    sec = []
    possible_message = []

    for i, x in enumerate(hash):        # divide hash into byte fractions
        if not i % 2 == 0:
            sec.append(hash[i-1] + hash[i])

    while len(possible_message) < len(hash_to_break)/2:
        for i, byte in enumerate(sec):
            pairs = find_letters(byte)

            if len(pairs) == 1 and not byte == '00' and int(byte, 16) <= 128:
                sorted = [pairs[0].pop(pairs[0].index(x)) for x in pairs[0] if not x == ' ']  # pop() every ' ' in 'pairs'

                possible_message.append(sorted[0])
            else:
                possible_message.append(str(i+1))

    message = ' - '.join(possible_message)
    return message


broken_message = breaker(hash_to_break)

print("\n=================================================================")
print("                        Broken message                           ")
print("=================================================================\n")
print(broken_message, '\n')