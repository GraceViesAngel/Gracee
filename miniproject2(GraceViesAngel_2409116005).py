from prettytable import PrettyTable

Nama_admin = "cici"
admin_Pasword = "admincici"
User = "user"
user_Pasword = "loginuser"

data_barang = []

def login():
    print("Login Sistem Penggadaian")
    print("Silahkan login terlebih dahulu")
    username = input("Username: ")
    password = input("Password: ")

    if username == Nama_admin and password == admin_Pasword:
        print(f"Login berhasil, selamat datang, {username}.")
        print("Saya telah menyediakan fasilitas ini untuk Anda yang ingin menggadaikan barang.")
        print("Terima kasih karena sudah mempercayakan program penggadaian kami. Ada yang bisa saya bantu?")
        return "admin"
    elif username == User and password == user_Pasword:
        print(f"Login berhasil, selamat datang, {username}.")
        return "user"
    else:
        print("Login gagal, periksa kembali username atau password.")
        return None

def admin_menu():
    while True:
        print("\n==== Menu Admin ====")
        print("1. Tambahkan Barang")
        print("2. Lihat Menu Barang")
        print("3. Perbarui Barang")
        print("4. Hapus Data Barang")
        print("5. Logout")
        pilih = input("Pilih satu opsi: ")

        if pilih == "1":
            tambah_barang()
        elif pilih == "2":
            lihat_menu_barang()
        elif pilih == "3":
            perbarui_barang()
        elif pilih == "4":
            hapus_data_barang()
        elif pilih == "5":
            print("Anda sudah keluar/logout.")
            break
        else:
            print("Pilihan tidak tersedia!!!")

def tambah_barang():
    nama_barang = input("Nama Barang: ")
    harga_barang = input("Harga Barang: ")
    data_barang.append({"nama": nama_barang, "harga": harga_barang})
    print("Barang sudah berhasil ditambahkan")

def lihat_menu_barang():
    if data_barang:
        table = PrettyTable()
        table.field_names = ["No", "Nama Barang", "Harga"]
        for idx, barang in enumerate(data_barang, 1):
            table.add_row([idx, barang["nama"], f"Rp. {barang['harga']}"])
        print(table)
    else:
        print("Tidak ada data barang")

def perbarui_barang():
    lihat_menu_barang()
    pilih = int(input("Pilih salah satu nomor yang ingin diubah atau diperbarui: ")) - 1
    if 0 <= pilih < len(data_barang):
        data_barang[pilih]["nama"] = input("Nama baru: ")
        data_barang[pilih]["harga"] = input("Harga baru: ")
        print("Data barang berhasil diubah")
    else:
        print("Nomor tidak valid")

def hapus_data_barang():
    lihat_menu_barang()
    pilih = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
    if 0 <= pilih < len(data_barang):
        del data_barang[pilih]
        print("Barang berhasil dihapus")
    else:
        print("Pilihan tidak valid!!!")

# User
def transaksi_menu():
    print("\n==== Menu Transaksi ====")
    nama = input("Nama lengkap penggadai: ")
    tempat_tanggal_lahir = input("Tanggal lahir (DD)(YYYY): ")
    pekerjaan = input("Pekerjaan: ")

    nama_barang = input("Masukkan nama barang yang ingin digadai: ")
    harga = int(input("Masukkan perkiraan harga barang yang digadai: Rp. "))
    pinjaman = int(input("Masukkan jumlah pinjaman yang Anda inginkan: Rp. "))

    if pinjaman > harga / 2:
        print("Maaf, tidak dapat meminjamkan uang sebesar itu. Harap menurunkan jumlah pinjaman Anda.")
        return
    else:
        print("Permintaan pinjaman Anda disetujui.")

    print("\n==== Pilihan Jangka Waktu ====")
    print("[a] 6 bulan dengan bunga 15%")
    print("[b] 12 bulan dengan bunga 20%")

    pilihan = input("Pilih jangka waktu (a/b): ")
    if pilihan == 'a':
        total_tempo = 0.15 * pinjaman + pinjaman
        tempo_bulanan = total_tempo / 6
        jangka = "6 Bulan"
    elif pilihan == 'b':
        total_tempo = 0.20 * pinjaman + pinjaman
        tempo_bulanan = total_tempo / 12
        jangka = "12 Bulan"
    else:
        print("Kode tidak valid!!!")
        return

    table = PrettyTable()
    table.field_names = ["Deskripsi", "Detail"]
    table.add_row(["Nama Lengkap", nama])
    table.add_row(["Tanggal Lahir", tempat_tanggal_lahir])
    table.add_row(["Pekerjaan", pekerjaan])
    table.add_row(["Harga Barang", f"Rp. {harga}"])
    table.add_row(["Jumlah Pinjaman", f"Rp. {pinjaman}"])
    table.add_row(["Tenor", jangka])
    table.add_row(["Pembayaran Bulanan", f"Rp. {tempo_bulanan:.2f}"])
    table.add_row(["Total Pembayaran", f"Rp. {total_tempo:.2f}"])
    print("\n==== Ringkasan Transaksi ====")
    print(table)

def main():
    user_type = login()
    if user_type == "admin":
        admin_menu()
    elif user_type == "user":
        transaksi_menu()
    else:
        print("Login gagal atau tidak ada akses.")

if __name__== "__main__":
    main()