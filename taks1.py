# Judul Program: Program Menghitung dan Mencetak Tanggal di Masa Depan

from datetime import datetime, timedelta

def print_future_date(days):
    # Dapatkan tanggal saat ini
    current_date = datetime.now()
    
    # Hitung tanggal di masa depan
    future_date = current_date + timedelta(days=days)
    
    # Definisikan daftar nama bulan untuk format
    month_names = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                   "Agustus", "September", "Oktober", "November", "Desember"]
    
    # Definisikan daftar nama hari untuk format
    weekday_names = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    # Format output tanggal 
    formatted_date = future_date.strftime("%A, %d %B %Y")
    
    print(formatted_date)

print("Program Menghitung dan Mencetak Tanggal di Masa Depan")

try:
    days = int(input("Masukkan jumlah hari dari sekarang: "))
    print_future_date(days)
except ValueError:
    print("Silakan masukkan jumlah hari yang valid.")
