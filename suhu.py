import os

def show_menu(): 
    print("======Selamat Datang Di Menu Konversi Suhu======")
    print("Berikut Pilihan Konversi")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")
    print("3. Celcius ke Kelvin")
    print("4. Kelvin ke Celcius")
    print("5. Celcius ke Reamur")
    print("6. Reamur ke Celcius")


def konversi ():
    print("Pilih Konversi Suhu yang Anda inginkan: ")
    angka = float(input("Masukkan nilai suhu: "))
    pilihan = int(input("Anda ingin Konversi ke Mana? : "))

    match pilihan:
        case 1:
            hasil = (angka * 9/5) + 32
            print(f"hasil konversi: {hasil} Fahrenheit")
        case 2:
            hasil = (angka - 32) * 5/9
            print(f"hasil konversi: {hasil} Celcius")
        case 3:
            hasil = (angka + 273.15)
            print(f"hasil konversi: {hasil} Kelvin")
        case 4:
            hasil = (angka - 273.15)
            print(f"hasil konversi: {hasil} Celcius")
        case 5:
            hasil = (angka * 4/5)
            print(f"hasil konversi: {hasil} Reamur")
        case 6:
            hasil = (angka * 5/4)
            print(f"hasil konversi: {hasil} Celcius")
        case _:
            print("Pilihan tidak valid, pililah yang ada di daftar")

def lanjut():
    while True:
        user_input = input("Apakah Ingin Melanjutkan Konversi Suhu? (y/n): ")
        match user_input:
            case 'y':
                os.system("cls")
                show_menu()
                konversi()

            case 'n':
                print(" Terima kasih! ")
                break

            case _:
                print("Pilihan tidak valid, pililah y/n!")


