# tulis solusi code disini

class Kalkulator:
    def __init__(key, x, y):
        key.x = x
        key.y = y
    def Penjumlahan(key):
        return key.x + key.y
    def Pengurangan(key):
        return key.x - key.y
    def Perkalian(key):
        return key.x * key.y
    def Pembagian(key):
        return key.x / key.y
def main():
    penjumlahan = Kalkulator(3, 4)
    pengurangan = Kalkulator(15, 4)
    perkalian = Kalkulator(10, 10)
    pembagian = Kalkulator(12, 3)

    print("Penjumlahan: ", penjumlahan.Penjumlahan())
    print("Pengurangan: ", pengurangan.Pengurangan())
    print("Perkalian: ", perkalian.Perkalian())
    print("Pembagian: ", pembagian.Pembagian())

if __name__ == "__main__":
    main()