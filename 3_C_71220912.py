q = str(input('Masukkan daftar pesanan: '))
b =("Daftar pesanan:" , (q.title()))
print (b)
z = input('Masukkan pesanan yang ingin ditambahkan: ')
if z == z in q:
    print( z.upper() , 'sudah berada dalam daftar pesanan')
else:
    print('Hasil penambahan pada daftar pesanan: ' , b , ',' , (z.title()))
