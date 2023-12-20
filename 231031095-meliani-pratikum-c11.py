import os
os.system('cls')


# PROGRAM BAGIAN PERTAMA 
nilai = 5

def hitung_faktorial(nilai):
    # Mencari Faktorial dengan input 
    if nilai > 1:
        return nilai * hitung_faktorial(nilai-1)
    return 1

# Program Utama 
faktorial = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')

# PROGRAM BAGIAN KEDUA
def hitung_faktorial(nilai):
    if nilai > 1:
        return nilai * hitung_faktorial(nilai-1)
    return 1

# Input nilai 
nilai = int(input("Masukkan nilai: "))  

# Hitung faktorial
faktorial = hitung_faktorial(nilai)

# Tampilkan hasil
print(f"Faktorial dari {nilai} adalah {faktorial}")

