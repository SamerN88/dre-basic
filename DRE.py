import random
from base_conversion import baseM_to_baseN


class DRE:
    def __init__(self, pt_symbols, ct_symbols):
        # Key is a combination of plaintext symbol set and ciphertext symbol set (both secret)
        self.key = (pt_symbols, ct_symbols)

    def encrypt(self, plaintext):
        pt_symbols, ct_symbols = self.key

        # Prepend random non-zero digit to plaintext to ensure the first character is not the 0th digit, since leading
        # zeros vanish upon base conversion (e.g. 0472 becomes 472 upon decryption using standard decimal)
        plaintext = random.choice(pt_symbols[1:]) + plaintext

        return baseM_to_baseN(plaintext, pt_symbols, ct_symbols)

    def decrypt(self, ciphertext):
        pt_symbols, ct_symbols = self.key
        return baseM_to_baseN(ciphertext, ct_symbols, pt_symbols)[1:]


def demo():
    # Choose plaintext symbol set and ciphertext symbol set
    pt_symbols = r'''E G)Z@o+."2i5;Q^6c~K}J9zXbIr&Fd4A'n_L,yfC*gx7#kTUDV1$SWhHjuOP%vwNt?-Ra:(><qps{B!m/Yl3M=e08'''
    ct_symbols = r'''<?pzL%B3W~qUSX;xPhVTH$s&:YMojuDd.7)kJ5IGN=>8n(4-1^g9A#'_@b+irl"ewc*QE0,aC}ym/KO'''

    dre = DRE(pt_symbols, ct_symbols)  # create DRE object
    plaintext = 'This is a secret message!'  # choose plaintext
    ciphertext = dre.encrypt(plaintext)  # encrypt plaintext
    decrypted = dre.decrypt(ciphertext)  # decrypt ciphertext
    print(decrypted == plaintext)  # check if decrypted text equals original plaintext


if __name__ == '__main__':
    demo()
