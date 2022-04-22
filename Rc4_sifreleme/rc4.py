import sifreleme
import sifrecozme
import sifrecozme2

def anahtar2():

    anahtar2='Yek'

    return anahtar2

def anahtar():

    anahtar='Key'

    return anahtar

if __name__ == '__main__' :

    anahtar = anahtar()
    anahtar2=anahtar2()
    düzmetin = 'Plaintext'
    sifreli_metin = sifreleme.sifreleme(anahtar, düzmetin)
    sifresi_cozulmus = sifrecozme.sifrecozme(anahtar, sifreli_metin)
    sifresi_cozulmus = sifrecozme2.sifrecozme(anahtar2, sifreli_metin)

    print("//////sifreleme_anahtarı:",anahtar)
    print("//////sifre_cözme_anahtarı:",anahtar2)
    print('/////düzmetin_hali:', düzmetin)
    print('/////sifreli_metin_hali:', sifreli_metin)
    print('/////sifresi_cözülmüs_hali:', sifresi_cozulmus)
