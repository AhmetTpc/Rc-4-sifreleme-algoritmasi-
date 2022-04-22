def KSA(anahtar):

    anahtar_uzunlugu = len(anahtar)
    A = [y for y in range(256)]
    x = 0
    for y in range(256):
        x = (x + A[y] + anahtar[y % anahtar_uzunlugu]) % 256
        A[y], A[x] = A[x], A[y]

    return A

def PRGA(S):

    x = 0
    y = 0
    while True:
        x= (x + 1) % 256
        y = (y + S[x]) % 256

        S[x], S[y] = S[y], S[x]
        K = S[(S[x] + S[y]) % 256]
        yield K

