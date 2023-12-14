import os
os.system ('cls')
import random as rd

print('Program tebak angkah dari 1 samapi 10')

angkah = [1,2,3,4,5,6,7,8,9,10]
tebak = rd.choice(angkah)
a = True
limit = 3
i = 0

while a:
    i +=1
    pilih = input('Masukkan pilihan angkah: ')
    if pilih == tebak:
        print(f'Pilihan anda benar yaitu {pilih}')
        a = False
    else:
        if i < limit:
            print('Tebakan andah salah! coba lagi')
            print(f'Kesempatan anda tersisa {limit-i} kali')
            a = True
        else:
            print('Kesempatan anda habis!')
            a = False
