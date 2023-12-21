data = {'nama'     : 'Meliani',
        'kelas'    : 'SI23C',
        'umur'     : '19 tahun',
        'anak ke'  : 'ketiga',
        'nim'      : '231031095',
        'jurusan'  : 'sains',
        'prodi'    : 'sistem informasi',
        'semester' : 'ganjil',
        'status'   : 'aktif',
        'angkatan' : '2023',
        'kota'     : 'parepare',
        'alamat'   : 'jalan industri',
        'hobi'     : 'membaca',
       }

print(data)
print(len(data))
print()

#Mengakses Dictionary
print(data.get('jurusan'))
print(data['semester'])
print()

#mengakses data
print(data['nama'])
print(data['nim'])
print(data['umur'])
print(data['kelas'])
print(data['prodi'])
print(data['angkatan'])
print(data['alamat'])
print(data['hobi'])
print()

#mengupdate dan menambah data
data['hobi'] = 'olahraga'
print(data)
print()

# Menghapus data
del data['anak ke']
print(data)
print()

#Nested Dictionary
bio_data = {'nama'     : 'Meliani',
            'nim'      : '231031095',
            'nilai'    : [98,96,95,99],
            'kesukaan' : {'makanan' : 'nasi goreng',
                          'minuman' : 'cokelat',
                          'hobi'    : 'membaca',
                          'warna'   : 'hitam'
                         }
           }
print(bio_data)
print()
print(bio_data['kesukaan']['warna'])
print(bio_data['kesukaan']['minuman'])
print(bio_data['kesukaan']['makanan'])
print(bio_data['nilai'][3])
print()

print(bio_data['kesukaan'].keys()) # melihat seluruh keys
print()

bio_data['kesukaan']['belajar'] = 'semua hal'
print(bio_data['kesukaan'].values()) # melihat seluruh nilai/value
