# tulis solusi code disini

class Persegi:
    def __init__(key, sisi):
        key.sisi = sisi
    def luas(key):
        return key.sisi ** 2
    def keliling(key):
        return 4 * key.sisi
    
class Segitiga:
    def __init__(key, alas, tinggi):
        key.alas = alas
        key.tinggi = tinggi
    def luas(key):
        return 0.5 * key.alas * key.tinggi
    def keliling(key):
        sisi_miring = (key.alas ** 2 + key.tinggi ** 2) ** 0.5
        return key.alas + key.tinggi + sisi_miring
    
class PersegiPanjang:
    def __init__(key, panjang, lebar):
        key.panjang = panjang
        key.lebar = lebar
    def luas(key):
        return key.panjang * key.lebar
    def keliling(key):
        return 2 * (key.panjang + key.lebar)
    
def main ():
    persegi = Persegi(5)
    segitiga = Segitiga(3,4)
    persegi_panjang = PersegiPanjang(4,6)

    print("Luas")
    print("Persegi :", persegi.luas())
    print("Segitiga :", segitiga.luas())
    print("Persegi Panjang :", persegi_panjang.luas())
    print("Keliling")
    print("Persegi :", persegi.keliling())
    print("Segitiga :", segitiga.keliling())
    print("Persegi Panjang :", persegi_panjang.keliling())

if __name__ == "__main__":
    main()
    
