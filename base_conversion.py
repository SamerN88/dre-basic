def base10(s, symbols):
    if len(symbols) != len(set(symbols)):
        msg = 'symbols must be distinct'
        raise ValueError(msg)

    base = len(symbols)

    max_pos = len(s) - 1
    result = 0
    for i in range(len(s)):
        pos = max_pos - i
        digit = symbols.index(s[i])
        result += digit * (base ** pos)

    return result


def baseN(n, symbols):
    if len(symbols) != len(set(symbols)):
        msg = 'symbols must be distinct'
        raise ValueError(msg)

    base = len(symbols)

    result = []
    while n > 0:
        digit = n % base
        result.append(symbols[digit])
        n //= base

    # If result is empty then n=0, so return the 0th digit of symbols
    return ''.join(reversed(result)) or symbols[0]


def baseM_to_baseN(s, symbols_M, symbols_N):
    return baseN(base10(s, symbols_M), symbols_N)

