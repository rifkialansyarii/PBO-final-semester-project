import os

def show_menu():
    print("======Selamat Datang Di Menu Konversi Waktu======")
    print("Berikut Pilihan Konversi")
    print("1. Detik Ke Menit")
    print("2. Menit Ke Detik")
    print("3. Menit Ke Jam")
    print("4. Jam Ke Menit")
    print("5. Detik Ke Jam")
    print("6. Jam Ke Detik")
    print("7. Hari Ke Jam")
    print("8. Hari Ke Detik")
    print("9. Hari Ke Menit")


def konversi():
    print("Pilih Konversi Waktu yang Anda inginkan: ")
    angka = int(input("Masukkan Angka yang ingin dikonversi: "))
    pilihan = int(input("Anda ingin Konversi ke Mana? : "))

    match pilihan:
        case 1:
            detik_ke_menit = round(angka / 60 ,2)
            print(f"Hasil konversi: {detik_ke_menit} menit")

        case 2:
            menit_ke_detik = angka * 60
            print(f"Hasil konversi: {menit_ke_detik} detik")

        case 3:
            menit_ke_jam = round(angka / 60 ,2)
            print(f"Hasil konversi: {menit_ke_jam} jam")

        case 4:
            jam_ke_menit = angka * 60
            print(f"Hasil konversi: {jam_ke_menit} menit")

        case 5:
            detik_ke_jam = round(angka / 3600 ,2)
            print(f"Hasil konversi: {detik_ke_jam} jam")

        case 6:
            jam_ke_detik = angka * 3600
            print(f"Hasil konversi: {jam_ke_detik} detik")
        case 7:
            hari_ke_jam = angka * 24
            print(f"Hasil Konversi: {hari_ke_jam} jam")
        case 8:
            hari_ke_detik = angka * 86400
            print(f"Hasil Konversi: {hari_ke_detik} detik")
        case 9:
            hari_ke_menit = angka * 24 * 60
            print(f"Hasil Konversi: {hari_ke_menit} menit")

        case _:
            print("Pilihan tidak valid!")

def lanjut():
    
    while True:
        user_input = input("Apakah Ingin Melanjutkan Konversi Waktu? (y/n): ")
        match user_input:
            case 'y':
                os.system('cls')
                show_menu()
                konversi()
            case 'n':
                print("Terima Kasih!")
                return False
            case _:
                print("Pilihan tidak valid, pililah y/n!")
                
