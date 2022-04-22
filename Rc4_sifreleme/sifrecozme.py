import xor
import codecs

def sifrecozme(anahtar2, sifreli_metin):

    sifreli_metin = codecs.decode(sifreli_metin, 'hex_codec')
    res = xor.lojik_sifreleme(anahtar2, sifreli_metin)

    return codecs.decode(res, 'hex_codec').decode('utf-8','replace')
