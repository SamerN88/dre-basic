import random
from base_conversion import baseM_to_baseN


class DRE:
    def __init__(self, pt_symbols, ct_symbols):
        # Key is a combination of plaintext symbol set and ciphertext symbol set (both secret)
        self.key = (pt_symbols, ct_symbols)

    def encrypt(self, plaintext):
        pt_symbols, ct_symbols = self.key

        # Prepend random non-zero digit to plaintext to ensure that first character is not 0th digit, since leading
        # zeros vanish upon base conversion (e.g. 0472 becomes 472 upon decryption using standard base-10)
        plaintext = random.choice(pt_symbols[1:]) + plaintext

        return baseM_to_baseN(plaintext, pt_symbols, ct_symbols)

    def decrypt(self, ciphertext):
        pt_symbols, ct_symbols = self.key
        return baseM_to_baseN(ciphertext, ct_symbols, pt_symbols)[1:]


def demo():
    print('Demo: how to use dre-basic')
    print('---\n')

    # Choose plaintext symbol set and ciphertext symbol set
    pt_symbols = r'''vZ5Q7hWgw=.G(2/4Y,zO+qNlH}"[`?)$V:ybeUj#]F680*ax@A-KSpf3'EPXBT;rD_LcJ^kC\d>&9Inuom<t%s~M!1i|{R'''
    ct_symbols = r'''fnwbmuyhcisgkpatxdevlzoqjr'''

    dre = DRE(pt_symbols, ct_symbols)  # create DRE object
    plaintext = 'This_is_a_secret_message!'  # choose plaintext
    ciphertext = dre.encrypt(plaintext)  # encrypt plaintext
    decrypted = dre.decrypt(ciphertext)  # decrypt ciphertext
    success = decrypted == plaintext  # check if decrypted text equals original plaintext

    print('1. Let\'s choose the following symbol sets to encrypt and decrypt with (these are SECRET):')
    print(f'\tPlaintext symbol set: (base-{len(pt_symbols)}) {pt_symbols}')
    print(f'\tCiphertext symbol set: (base-{len(ct_symbols)}) {ct_symbols}')

    print('\n')

    print('2. We now create our DRE object with the following code:')
    print('```')
    print(f"pt_symbols = r'''{pt_symbols}'''")
    print(f"ct_symbols = r'''{ct_symbols}'''")
    print('dre = DRE(pt_symbols, ct_symbols)')
    print('```')

    print('\n')

    print('3. Note that our key is a combination of both the plaintext symbol set and the ciphertext symbol set:')
    print('\tKey:')
    print('\t(')
    print(f'\t\t{dre.key[0]},')
    print(f'\t\t{dre.key[1]}')
    print('\t)')

    print('\n')

    print(f'4. Now let\'s choose the following plaintext, which uses the base-{len(pt_symbols)} symbol set above:')
    print('```')
    print(f'plaintext = \'{plaintext}\'')
    print('```')

    print('\n')

    print('5. Encrypt:')
    print('```')
    print('ciphertext = dre.encrypt(plaintext)')
    print()
    print('ciphertext')
    print(f'>>> {ciphertext}')
    print('```')

    print('\n')

    print('6. Decrypt:')
    print('```')
    print('decrypted = dre.decrypt(ciphertext)')
    print('```')

    print('\n')

    print('7. We can check if the system was successful:')
    print('```')
    print('decrypted == plaintext')
    print(f'>>> {success}')
    print('```')

    print()

    print(f'The system {"worked" if success else "did not work"}.')


if __name__ == '__main__':
    demo()
