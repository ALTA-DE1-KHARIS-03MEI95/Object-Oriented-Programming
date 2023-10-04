# tulis solusi code disini

class OngkosKirim:
    def __init__(key, panjang, lebar, tinggi, berat):
        key.panjang = panjang
        key.lebar = lebar
        key.tinggi = tinggi
        key.berat = berat

    def harga(key):
        volume = key.panjang * key.lebar * key.tinggi
        if volume < 50 or key.berat < 1:
            return 5000
        else:
            return 5000 * (volume/50) * key.berat
def main():
    ongkos = OngkosKirim(5,2,4,1)
    
    print("Harga: Rp.", ongkos.harga())
if __name__ == "__main__":
    main()