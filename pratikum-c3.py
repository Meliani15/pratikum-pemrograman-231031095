print ('PRATIKUM 3')

nama = 'meliani'
nim = '231031095'
meet = 'Pratikum 3 (String)'
prodi = 'Sistem Informasi C'
email = 'amnmeli123@gmail.com'
sp = 150

print("-"*150)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)


nama = 'MELIANI'
nim  = '231031095'
meet = 'Praktikum 3 (String)'
prodi= 'Sistem Informasi C'
email= 'amnmeli123@gmail.com'
ttl = '15-05-2004'
alamat = 'Jl. Industri'
asal = 'Mamasa'
hobi = 'Membaca'
tinggi = 157

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima kasih.\n''')

print(f'''Biodata saya,
Nama\t: {nama.upper()}
NIM\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
hobi\t: {hobi}
tinggi\t: {tinggi}cm
      ''')

#TUGAS
stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir
a = stat1.split()
stat1 = ' '.join([a[-1], a[0], a[1], a[2]])
print(stat1)
print()

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac
a = stat2.split()
stat2 = ' '.join(['duFort'[0], 'Frankel'[0], 'Sir'[0], 'Issac'])
print(stat2)
print()

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I
stat3 = ' '.join(['duFort', 'Frankel'[0], 'Sir'[0], 'Issac'[0]])
print(stat3)
print()

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir
a = stat4.split()
stat4 = ' '.join([a[-1][0], a[0], a[1], a[2]])
print(stat4)
print()

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S
a = stat5.split()
stat5 = ' '.join([a[-1], a[0][0], a[1][0], a[2][0]])
print(stat5)
print()

stat6 = ['duFort Frankel Sir Issac']
# ISSAC D F S
stat6 = ' '.join([a[-1], a[0][0], a[1][0], a[2][0]]).upper()
print(stat6)
print()

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
a =stat7.strip ('#,$')
print(a)
print()

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
b = a.strip ('#,$')
print(b)
print()

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
b = a.strip ('#,@,$')
print(b)
print()

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
b = a.strip ('#,@,$').upper()
print(b)
print()