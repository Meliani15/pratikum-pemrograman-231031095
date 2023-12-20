 
print("Nama : MELIANI")
print("NIM : 231031095")
print("Prodi : Sistem Informasi")
print("Tanggal Lahir : 15-05-2004")

print()
print()
 # Operasi aritmatika
a =95
print ('Nilai a =',a )
a =95
a +=1
print ('Nilai a +=1 akan menjadi ',a)
a =95
a -=1
print ('Nilai a -=1 akan menjadi ',a)
a =95
a *=2
print ('Nilai a *=2 akan menjadi ',a)
a =95
a /=2
print ('Nilai a /=2 akan menjadi ',a)
a =95
a %=2
print ('Nilai a %=2 akan menjadi ',a)
a =95
a //=2
print ('Nilai a //=2 akan menjadi ',a )
a =95
a **=2
print ('Nilai a **=2 akan menjadi ',a )
#OR
b = True
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi ',b )
b = False
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi ',b )
# AND
b = True
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi ',b )
b = False
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi ',b )
# XOR
b = True
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi ',b )
b = False
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi ',b )
# Shifting
c =0b0100
print ('Nilai c =',format (c , '04b') )
c >>=1
print ('Nilai c > >=1 akan menjadi ',format (c , '04b') )
c =0b0100
c <<=1
print ('Nilai c < <=1 akan menjadi ',format (c , '04b') )
print()
print()
#oprrasi perbandingan
a =5 # isi dengan ujung NIM
b =10 # Ubah dengan hasil jumlah ujung NIM dengan 5
print (' ================== Besar dari 10 ')
hasil = a >10
print (a ,'> 10 adalah ', hasil )
hasil = b >10
print (b ,'> 10 adalah ', hasil )
print()
print (' ================== Kecil dari 10 ')
hasil = a <10
print (a ,'< 10 adalah ', hasil )
hasil = b <10
print (b ,'< 10 adalah ', hasil )
print()
print (' ================== Besar atau sama dari 10 ')
hasil = a >=10
print (a ,' >= 10 adalah ', hasil )
hasil = b >=10
print (b ,' >= 10 adalah ', hasil )
print()
print (' ================== Besar atau sama dari 10 ')
hasil = a <=10
print (a ,' <= 10 adalah ', hasil )
hasil = b <=10
print (b ,' <= 10 adalah ', hasil )
print()
print (' ================== Sama dengan 10 ')
hasil = a ==10
print (a ,'== 10 adalah ', hasil )
hasil = b ==10
print (b ,'== 10 adalah ', hasil )
print()
print (' ================== Tidak sama dengan 10 ')
hasil = a !=10
print (a ,'!= 10 adalah ', hasil )
hasil = b !=10
print (b ,'!= 10 adalah ', hasil )
print()
#operasi Logika
print (' ============= NOT ============= ')
a = True
c = not a
print ('a adalah ',a )
print (' ------c = not a- - - -- - - NOT ')
print ('c adalah ',c )
print()
print (' ============= OR ============= ')
a = True
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )
print()
a = True
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )
print()
a = False
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )
print()
a = False
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )
print()
print (' ============= AND ============= ')
a = True
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )
print()
a = True
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )
print()
a = False
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )
print()
a = False
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )
print()
print (' ============= XOR ============= ')
a = True
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
print()
a = True
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
print()
a = False
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
print()
a = False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
print()
print()
#Operasi Membership
print (' ======================= IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test = 'rud '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test = 'bac '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
print (' ======================= NOT IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test = 'rud '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test = 'bac '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
print()
print()

#Tugas Pratikum operator logika
a=True
b=False
print('\n============NAND============')
hasil=not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil=not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil=not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil=not (b and b)
print(b,'nand',b,'adalah =',hasil)
print()
print('\n============NOR============')
hasil=not (a or a)
print(a,'xor',a,'adalah =',hasil)
hasil=not (a or b)
print(a,'xor',b,'adalah =',hasil)
hasil=not (b or a)
print(b,'xor',a,'adalah =',hasil)
hasil=not (b or b)
print(b,'xor',b,'adalah =',hasil)
print()
print('\n============NXOR============')
hasil=not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil=not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil=not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil=not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)
print()
print()

#Tugas Operator Membership
print (' ======================= IN ')
nama_lengkap = 'Meliani'
test1 = 'Me'
cek = test1 in nama_lengkap
print ( test1 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test2 = 'eM'
cek = test2 in nama_lengkap
print ( test2 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test3 = 'a'
cek = test3 in nama_lengkap
print ( test3 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test4 = 'i'
cek = test4 in nama_lengkap
print ( test4 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test5 = 'u'
cek = test5 in nama_lengkap
print ( test5 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test6 = 'e'
cek = test6 in nama_lengkap
print ( test6 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
test7 =  'o'
cek = test7 in nama_lengkap
print ( test7 +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )
print()
print (' ======================= NOT IN ')
nama_lengkap = ' Meliani '
test1 = 'Me'
cek = test1 not in nama_lengkap
print ( test1 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test2 = 'eM'
cek = test2 not in nama_lengkap
print ( test2 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test3 = 'a'
cek = test3 not in nama_lengkap
print ( test3 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test4 = 'i'
cek = test4 not in nama_lengkap
print ( test4 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
test5 = 'u'
cek = test5 not in nama_lengkap
print ( test5 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
print()
test6 = 'e'
cek = test6 not in nama_lengkap
print ( test6 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )
test7 = 'o'
cek = test7 not in nama_lengkap
print ( test7 +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )





