daftarPelanggan = []

while True:
    print("==========Antrian Pembelian Makanan===========")
    print("Menu Antrian:")
    print("1. Tambah Pelanggan")
    print("2. Tampilkan Antrian")
    print("3. Cari Pelanggan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == '1':
        nama = input("Masukkan nama pelanggan: ")
        umur = int(input("Masukkan umur pelanggan: "))
        daftarPelanggan.append([nama, umur])
        print("Pelanggan berhasil ditambahkan!\n")
    
    elif pilihan == '2':
        print("\nAntrian berdasarkan urutan masuk:")
        for pelanggan in daftarPelanggan:
            print(f"{pelanggan[0]}\t{pelanggan[1]}")
        
        descPelanggan = daftarPelanggan[:]
        n = len(descPelanggan)
        for i in range(n-1, 0, -1):
            for j in range(i):
                if descPelanggan[j][1] < descPelanggan[j+1][1]:
                    descPelanggan[j], descPelanggan[j+1] = descPelanggan[j+1], descPelanggan[j]

        print("\nAntrian berdasarkan umur (desc):")
        for pelanggan in descPelanggan:
            print(f"{pelanggan[0]}\t{pelanggan[1]}")
        print()
    
    elif pilihan == '3':
        nama_cari = input("Masukkan nama pelanggan yang dicari: ")
        
        ada = False
        for i in daftarPelanggan:
            if i[0] == nama_cari:
                ada = True
                break
        
        if ada :
            index = 1
            for pelanggan in daftarPelanggan:
                if pelanggan[0] == nama_cari:
                    print(f"Berdasarkan urutan masuk : {nama_cari} ditemukan pada antrian nomor {index}")
                    break
                index += 1


            descPelanggan = daftarPelanggan[:]
            n = len(descPelanggan)
            for i in range(n-1, 0, -1):
                for j in range(i):
                    if descPelanggan[j][1] < descPelanggan[j+1][1]:
                        descPelanggan[j], descPelanggan[j+1] = descPelanggan[j+1], descPelanggan[j]
            
            index = 1
            for pelanggan in descPelanggan:
                if pelanggan[0] == nama_cari:
                    print(f"Berdasarkan umur (prioritas lebih tua) : {nama_cari} ditemukan pada antrian nomor {index}")
                    break
                index += 1


        else :
            print("Nama Pelanggan tidak ditemukan diantrian")
        
        
    
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
