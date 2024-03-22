# Judul Program: Menghitung Rata-rata Inputan Pengguna

def main():
    grades = []  # List untuk menyimpan nilai-nilai
    grade_sum = 0  # Variabel untuk menjumlahkan total nilai
    count = 0  # Variabel untuk menghitung jumlah nilai
    
    # Mengambil input nilai sampai -1 dimasukkan
    while True:
        grade = input("Masukkan nilai (atau -1 untuk selesai): ")
        if grade == '-1':
            break
        else:
            grades.append(int(grade))  # Menambahkan nilai ke dalam list
            grade_sum += int(grade)  # Menambahkan nilai ke total
            count += 1  # Menambahkan 1 ke jumlah nilai
    
    # Menghitung rata-rata
    if count > 0:
        average = grade_sum // count
    else:
        average = 0
    
    # Output rata-rata
    print("Rata-rata:", average)
    
    # Output nilai-nilai sesuai dengan urutan masukkan
    for grade in grades:
        print(grade)

if __name__ == "__main__":
    print("Judul Program: Menghitung Rata-rata Inputan Pengguna") 
    main()
