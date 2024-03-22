def main():
    total = 0  # Variabel untuk menyimpan total nilai
    while True:
        try:
            num = float(input("Masukkan angka (masukkan -1 untuk berhenti): "))  # Input dari user
            if num == -1:  
                break
            total += num  
        except ValueError:  
            print("Silakan masukkan angka yang valid.")
    
    print(f"Total semua angka yang dimasukkan adalah: {total:.2f}")  # Output Program

if __name__ == "__main__":
    print("Program menghitung semua input user") 
    main()
