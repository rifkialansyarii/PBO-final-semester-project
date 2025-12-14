import os

def show_menu():
    print("===Test Konversi Berat===")
    print("Pilihan Satuan: Miligram, Gram, Kilogram, Kwintal")
    print("1.Miligram ke Gram")
    print("2.Gram ke Kilogram")
    print("3.Kilogram Ke Kwintal")



def konversi():
    print("Pilihlah Konversi Berat yang Inginkan:")
    Angka = int(input("Masukkan Berapa Yang Ingin Di Konversikan:"))
    Pilihan = int(input("Masukkan Pilihan Konversi Berat (1/2/3):"))

    match Pilihan:
        case 1:
            Miligram_ke_Gram = round(Angka / 1000, 2)
            print(f"{Angka} Miligram = {Miligram_ke_Gram} Gram")
        case 2:
            Gram_ke_Kilogram = round(Angka / 1000, 2)
            print(f"{Angka} Gram = {Gram_ke_Kilogram} Kilogram")
        case 3:
            Kilogram_ke_Kwintal = round(Angka / 100, 2)
            print(f"{Angka} Kilogram = {Kilogram_ke_Kwintal} Kwintal")
        case _:
            print("Pilihan Tidak Tersedia")

def lanjut():
    while True:
        user_input = input("Apakah Ingin Melanjutkan Konversi Berat? (y/n): ").lower()
        match user_input:
            case 'y':
                os.system('cls')
                show_menu()
                konversi()
            case 'n':
                print("Terima Kasih Telah Menggunakan Program Konversi Berat")
                break
            case _:
                print("Input Tidak Valid, Silahkan Masukkan 'y' atau 'n'")