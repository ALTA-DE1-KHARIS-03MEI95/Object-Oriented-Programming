# tulis solusi code disini

import math

class Kubus:
    def __init__(key, sisi):
        key.sisi = sisi
    def volume(key):
        return key.sisi ** 3
    
class Balok:
    def __init__(key, panjang, lebar, tinggi):
        key.panjang = panjang
        key.lebar = lebar
        key.tinggi = tinggi
    def volume(key):
        return key.panjang * key.lebar * key.tinggi
    
class Tabung:
    def __init__(key, jari_jari, tinggi):
        key.jari_jari = jari_jari
        key.tinggi = tinggi
    def volume(key):
        return math.ceil(math.pi * key.jari_jari**2 * key.tinggi)
    
def main ():
    kubus = Kubus(10)
    balok = Balok(3,6,10)
    tabung = Tabung(7, 10)

    print("Volume")
    print("Kubus: ", kubus.volume())
    print("Balok: ", balok.volume())
    print("Tabung:", tabung.volume())
    
if __name__ == "__main__":
    main()
    
