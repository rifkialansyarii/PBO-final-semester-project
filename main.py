import requests, time, os, suhu, waktu, berat
from tqdm import tqdm

class SmartConversion():
    def show_loading_screen(self):
        os.system('cls')

        resp = requests.get('https://asciified.thelicato.io/api/v2/ascii?text=%23Smart%20Converter/')
        print(resp.text)
        print('\033[1m' + 'Project By UHUYYY\n' + '\033[0m')

        for i in tqdm(range(50), desc='Loading'):
            time.sleep(0.1)
    
    def show_menu_conversion(self):
        os.system('cls')

        print(" ===Daftar Pilihan Konversi=== ")
        print('1. Konversi Suhu')
        print('2. Konversi Waktu')
        print('3. Konversi Berat')
        print('4. Konversi Panjang')
        print('5. Keluar')

    def conversion(self):
        self.show_menu_conversion()
        self.conversion_options = input('Pilih menu: ')

        match self.conversion_options:
            case '1':
                os.system('cls')
                
                suhu.show_menu()
                suhu.konversi()
                suhu.lanjut()

                self.conversion()
            case '2':
                os.system('cls')

                waktu.show_menu()
                waktu.konversi()
                waktu.lanjut()

                self.conversion()
            case '3':
                os.system('cls')

                berat.show_menu()
                berat.konversi()
                berat.lanjut()

                self.conversion()
            case '4':
                pass
                # os.system('cls')

                # panjang.show_menu()
                # panjang.konversi()
                # panjang.lanjut()
            case '5':
                os.system('cls')
                print('Terima kasih telah menggunakan program smart converter!')
                return
            case _:
                print('Inputan Anda Tidak valid')
            
if __name__ == '__main__':
    conversion1 = SmartConversion()
    conversion1.show_loading_screen()
    conversion1.conversion()
        
