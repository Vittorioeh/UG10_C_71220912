n = str(input('Masukkan Bulan (1-12): '))

if n == '1' or n == '3' or n == '5' or n =='7' or n == '8' or n == '10' or n == '12':
    print ('Jumlah Hari: 31')
elif n == '4' or n == '6' or n == '9' or n == '11':
    print ('Jumlah Hari: 30')
else:
    print ('Jumlah Hari: 28')
    
