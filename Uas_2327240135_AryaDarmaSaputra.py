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
        
        CiriPelanggan = daftarPelanggan[:]
        n = len(CiriPelanggan)
        for i in range(n-1, 0, -1):
            for j in range(i):
                if CiriPelanggan[j][1] < CiriPelanggan[j+1][1]:
                    CiriPelanggan[j], CiriPelanggan[j+1] = CiriPelanggan[j+1], CiriPelanggan[j]

        print("\nAntrian berdasarkan umur (ciri):")
        for pelanggan in CiriPelanggan:
            print(f"{pelanggan[0]}\t{pelanggan[1]}")
        print()
    
    elif pilihan == '3':
        CariPelanggan = input("Masukkan nama pelanggan yang dicari: ")
        
        ada = False
        for i in daftarPelanggan:
            if i[0] == CariPelanggan:
                ada = True
                break
        
        if ada :
            index = 1
            for pelanggan in daftarPelanggan:
                if pelanggan[0] == CariPelanggan:
                    print(f"Berdasarkan urutan masuk : {CariPelanggan} ditemukan pada antrian nomor {index}")
                    break
                index += 1


            CiriPelanggan = daftarPelanggan[:]
            n = len(CiriPelanggan)
            for i in range(n-1, 0, -1):
                for j in range(i):
                    if CiriPelanggan[j][1] < CiriPelanggan[j+1][1]:
                        CiriPelanggan[j], CiriPelanggan[j+1] = CiriPelanggan[j+1], CiriPelanggan[j]
            
            index = 1
            for pelanggan in CiriPelanggan:
                if pelanggan[0] == CariPelanggan:
                    print(f"Berdasarkan umur (prioritas lebih tua) : {CariPelanggan} ditemukan pada antrian nomor {index}")
                    break
                index += 1


        else :
            print("Nama Pelanggan tidak ditemukan diantrian")
        
        
    
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
