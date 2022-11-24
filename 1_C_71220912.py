print ('='*10 , 'Pilih menu' '='*10)
print ('1. Tambah')
print ('2. Kurang')
print ('3. Kali')
print ('4. Bagi')
a = int(input('Masukkan Angka Pertama: '))
b = int(input('Masukkan Angka Kedua: '))
pilih = input ('Pilihan Anda: ')

if pilih == '1':
    print('hasil =' , a + b)
elif pilih == '2':
    print('hasil =' , a - b)
elif pilih == '3':
    print('hasil =' , a * b)
else:
    print('hasil =' , float (a / b))
