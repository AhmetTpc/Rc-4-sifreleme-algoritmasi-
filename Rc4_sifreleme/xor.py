import anahtar_olusturma

def lojik_sifreleme(anahtar2, text):
    anahtar = [ord(c) for c in anahtar2]
    S = anahtar_olusturma.KSA(anahtar)
    keystream = anahtar_olusturma.PRGA(S)
    res = []

    for c in text:
        y=(c ^ next(keystream))
        val = ("%02x" % y)
        res.append(val)

    return ''.join(res)