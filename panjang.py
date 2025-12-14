import os

def show_menu():
    print("=== Test Konversi Panjang ===")
    print("Pilihan Satuan: Meter, Kilometer, Centimeter, Inch")
    print("1. Meter ke Kilometer")
    print("2. Kilometer ke Meter")
    print("3. Centimeter ke Meter")
    print("4. Meter ke Centimeter")
    print("5. Inch ke Centimeter")
    print("6. Centimeter ke Inch")

def konversi():
        angka = float(input("Masukkan nilai panjang yang ingin dikonversikan: "))
        pilihan = int(input("Masukkan pilihan konversi panjang (1-6): "))

        match pilihan:
            case 1:
                hasil = round(angka / 1000, 2)
                print(f"{angka} Meter = {hasil} Kilometer")
            case 2:
                hasil = round(angka * 1000, 2)
                print(f"{angka} Kilometer = {hasil} Meter")
            case 3:
                hasil = round(angka / 100, 2)
                print(f"{angka} Centimeter = {hasil} Meter")
            case 4:
                hasil = round(angka * 100, 2)
                print(f"{angka} Meter = {hasil} Centimeter")
            case 5:
                hasil = round(angka * 2.54, 2)
                print(f"{angka} Inch = {hasil} Centimeter")
            case 6:
                hasil = round(angka / 2.54, 2)
                print(f"{angka} Centimeter = {hasil} Inch")
            case _:
                print("Pilihan Tidak Tersedia")


def lanjut():
    while True:
        user_input = input("Apakah Ingin Melanjutkan Konversi Panjang? (y/n): ").lower()
        match user_input:
            case 'y':
                os.system('cls')
                show_menu()
                konversi()
            case 'n':
                print("Terima Kasih Telah Menggunakan Program Konversi Panjang")
                break
            case _:
                print("Input Tidak Valid, Silahkan Masukkan 'y' atau 'n'")
