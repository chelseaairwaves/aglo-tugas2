# Meminta input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang (cm): "))  # 28 cm
lebar = float(input("Masukkan lebar persegi panjang (cm): "))      # 14 cm

# Menghitung jari-jari lingkaran
r = lebar / 2

# Menghitung luas persegi panjang
luas_persegi_panjang = panjang * lebar

# Menghitung luas lingkaran penuh
luas_lingkaran = 3.14 * (r ** 2)

# Menghitung luas daerah yang diarsir
luas_arsir = luas_persegi_panjang - luas_lingkaran

# Menampilkan hasil
print("Luas daerah yang diarsir adalah:", luas_arsir, "cm²")




