import xor
import codecs
import rc4

def sifrecozme(anahtar2, sifreli_metin):

     if rc4.anahtar()!=anahtar2:
         print("\n Gelen anahtar, doğru anahtar ile aynı değil!! \n")
         exit()

     else :
        sifreli_metin = codecs.decode(sifreli_metin, 'hex_codec')
        res = xor.lojik_sifreleme(anahtar2, sifreli_metin)

        return codecs.decode(res, 'hex_codec').decode('utf-8','replace')
