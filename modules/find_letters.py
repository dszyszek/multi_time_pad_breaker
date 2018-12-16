import random
import itertools

list_of_bins = []
list_of_pairs = []
# what_value = input('Type the hex value of letter from xor you are breaking (you can break only one letter at time)\n')

ascii_table_all = {
    "A": "1000001", "B": "1000010", "C": "1000011", "D": "1000100", "E": "1000101", "F": "1000110", "G": "1000111", "H": "1001000", "I": "1001001", "J": "1001010", "K": "1001011", "L": "1001100", "M": "1001101", "N": "1001110", "O": "1001111", "P": "1010000", "Q": "1010001", "R": "1010010", "S": "1010011", "T": "1010100", "U": "1010101", "V": "1010110", "W": "1010111", "X": "1011000", "Y": "1011001", "Z": "1011010", "a": "1100001", "b": "1100010", "c": "1100011", "d": "1100100", "e": "1100101", "f": "1100110", "g": "1100111", "h": "1101000", "i": "1101001", "j": "1101010", "k": "1101011", "l": "1101100", "m": "1101101", "n": "1101110", "o": "1101111", "p": "1110000", "q": "1110001", "r": "1110010", "s": "1110011", "t": "1110100", "u": "1110101", "v": "1110110", "w": "1110111", "x": "1111000", "y": "1111001", "z": "1111010", "!": "0100001", "&": "0100110", "(": "0101000", ")": "0101001", ",": "0101100", ".": "0101110", "0":	"0110000", "1":	"0110001", "2":	"0110010", "3":	"0110011", "4":	"0110100", "5":	"0110101", "6":	"0110110", "7":	"0110111", "8":	"0111000", "9":	"0111001", ":":	"0111010", "?":	"0111111", " ": "00100000", "\"": "0100010", "\'": "0100111"
}

ascii_table = {"A": "1000001", "B": "1000010", "C": "1000011", "D": "1000100", "E": "1000101", "F": "1000110", "G": "1000111", "H": "1001000", "I": "1001001", "J": "1001010", "K": "1001011", "L": "1001100", "M": "1001101", "N": "1001110", "O": "1001111", "P": "1010000", "Q": "1010001", "R": "1010010", "S": "1010011", "T": "1010100", "U": "1010101", "V": "1010110", "W": "1010111", "X": "1011000", "Y": "1011001", "Z": "1011010", "a": "1100001", "b": "1100010", "c": "1100011", "d": "1100100", "e": "1100101", "f": "1100110", "g": "1100111", "h": "1101000", "i": "1101001", "j": "1101010", "k": "1101011", "l": "1101100", "m": "1101101", "n": "1101110", "o": "1101111", "p": "1110000", "q": "1110001", "r": "1110010", "s": "1110011", "t": "1110100", "u": "1110101", "v": "1110110", "w": "1110111", "x": "1111000", "y": "1111001", "z": "1111010", " ": "00100000"}



def xorF(stra, strb):
    stra = sameLength(stra, 7)
    strb = sameLength(strb, 7)
    return ''.join(hex(int(a, 16) ^ int(b, 16))[2:] for a, b in zip(stra, strb))

def sameLength(str, leng):
    while len(str) < leng:
        str = '0' + str
    return str


def main(hexIn):
    list_of_pairs.clear()
    list_of_bins.clear()
    counter = 0

    global list_of_combinations

    while not len(list_of_bins) == 128:

        for x in itertools.combinations(range(0, 128), 2):
            bin_a = bin(x[0])[2:]
            bin_b = bin(x[1])[2:]

            bin_hex = bin(int(str(hexIn), 16))[2:]

            bin_a = sameLength(bin_a, 7)
            bin_b = sameLength(bin_b, 7)
            bin_hex = sameLength(bin_hex, 7)

            if xorF(bin_a, bin_b) == bin_hex and not [bin_a, bin_b] in list_of_bins:
                list_temp = [bin_a, bin_b]
                list_of_bins.append(list_temp)
            counter += 1

        for x in list_of_bins:
            x0 = sameLength(str(x[0]), 7)
            x1 = sameLength(str(x[1]), 7)

            if chr(int(x0, 2)) in ascii_table and chr(int(x1, 2)) in ascii_table:
                list_of_pairs.append([chr(int(x0, 2)), chr(int(x1, 2))])           # output: ASCII
                # list_of_pairs.append([hex(int(x0, 2))[2:], hex(int(x1, 2))[2:]])    # output: HEX

        # print("\n----------------------------------\n")
        # print('Possible matches: ', list_of_pairs)
        # print('Length: ', len(list_of_pairs))
        return list_of_pairs


# main(what_value)