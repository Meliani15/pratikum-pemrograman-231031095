import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','9','5']
nim_sambung = ''.join(nim) 

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')


data = ['meliani',2023,'Aktif']
nilai= [90,89,93,97]
print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print(f'meliani status kuliah: {data[2]}')
print(f'data terbesar nilai adalah: {max(nilai)}')
print(f'data terkecil nilai adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')



data = [['meliani',2023,'Aktif'],
[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
data.append(11)
# Nama mahasiswa : meliani
print(f'Nama mahasiswa: {data[0][0]}')
# Inisial meliani: m
print(f'inisial meliani: {data[0][0][0]}')
# Nim meliani: 231031095
print(f'Nim meliani: {(nim_sambung)}')
#Program meliani: S1-Reguler Sistem Informasi 2023
print(f'Program meliani: {(data[3][0])} Sistem Informasi B {(data[0][1])}')
# Angkatan meliani: Ganjil-2023
print(f'Angkatan meliani: {(data[3][1])}-{(data[0][1])}')
# Total sks meliani adalah: 11
print(f'Total sks meliani adalah: {(data[4])}')   
# Jumlah Nilai meliani: 5
print(f'Jumlah nilai meliani adalah: {len(data[1]+[2])}')
# Nilai tertinggi meliani: 97
print(f'Nilai tertinggi meliani adalah: {max(data[1])}')
# Nilai terendah meliani: 89
print(f'Nilai terendah meliani adalah: {min(data[1])}')
# Rata-rata nilai meliani: 92.25
print(f'Nilai tertinggi meliani adalah: {sum(data[1])/len(data[1])}')
print()
print()

matkul = ['pengantar program',
          'kalkulus dasar',
          'bahasa',
          'sains terpadu',
          'pengantar teknologi informasi']
matkul.append('agama kristen')
matkul.append('pancasila')
matkul.append('wawasan cinta iptek dan imtaq')

sks = [2,3,2,3,3]
sks.append('3')
sks.append('2')
sks.append('3')

# Daftar Mata kuliah
print(f'Daftar Mata Kuliah')
# Mata kuliah 1: bahasa dengan jumlah 2 sks
print(f'Mata kuliah 1: {matkul[2]} dengan jumlah {sks[0]} sks')
# Mata kuliah 2: pengantar program dengan jumlah 3 sks
print(f'Mata kuliah 2: {matkul[0]} dengan jumlah {sks[1]} sks')
# Mata kuliah 3: sains terpadu dengan jumlah 2 sks
print(f'Mata kuliah 3: {matkul[3]} dengan jumlah {sks[2]} sks')
# Mata kuliah 4: pengantar teknologi informasi dengan jumlah 3 sks
print(f'Mata kuliah 4: {matkul[4]} dengan jumlah {sks[3]} sks')
# Mata kuliah 5: kalkulus dasar dengan jumlah 3 sks
print(f'Mata kuliah 5: {matkul[1]} dengan jumlah {sks[4]} sks')
# Mata kuliah 6: agama kristen dengan jumlah 2 sks
print(f'Mata kuliah 6: {matkul[5]} dengan jumlah {sks[6]} sks')
# Mata kuliah 7: pancasila dengan jumlah 3 sks
print(f'Mata kuliah 7: {matkul[6]} dengan jumlah {sks[7]} sks')
# Mata kuliah 8: wawasan cinta iptek dan imtaq dengan jumlah 3 sks
print(f'Mata kuliah 8: {matkul[7]} dengan jumlah {sks[5]} sks')
