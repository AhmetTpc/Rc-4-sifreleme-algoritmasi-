import xor

def sifreleme(anahtar, düz_metin):

    düz_metin = [ord(c) for c in düz_metin]

    return xor.lojik_sifreleme(anahtar, düz_metin)
