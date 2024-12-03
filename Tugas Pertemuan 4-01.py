#input nama 
nama = input("Nama : ")

#input alamat
alamat = input("Alamat : ")

#input tahun kelahiran 
tahun_kelahiran = int(input("Tahun Kelahiran :"))

#output nama 
print("Nama : ", nama)
#output alamat
print("Alamat : ", alamat)
#output tahun kelahiran 
print("Tahun Kelahiran : ", tahun_kelahiran)


import datetime
tahun_sekarang = datetime.datetime.now().year  # Mendapatkan tahun saat ini
umur = tahun_sekarang - tahun_kelahiran  # Menghitung umur
print(f"Umur : {umur} ")
