import copy
import datetime

rekamMedis=[
    {'IDRekam':4 ,'IDPasien': 7,'Nama':'Sequilla',
     'Status': 'Rawat Jalan','Diagnosa':'Rematik',
     'Dokter': 'Arie Gunawan', 'Tanggal':datetime.date(2023,11,19)}
]

dataKolom={
    'namaKolom':['IDRekam','IDPasien','Nama','Status','Diagnosa','Dokter','Tanggal'],
    'tipeKolom':['int','int','str','str','str','str','date'],
    'protect':[True,True,False,False,False,True,True]
}

 

def tampilEntri(penyakit='semua',pasien=0,noRekamMed=0,listMedis=rekamMedis):
    hasilFilter=[]
    if penyakit!='semua':
        for x in listMedis:
            if x.get('Diagnosa')==penyakit:
                hasilFilter.append(copy.deepcopy(x))
    elif pasien!=0:
        for x in listMedis:
            if x.get('IDPasien')==pasien:
                hasilFilter.append(copy.deepcopy(x))
        print('Nomor Pasien : {}'.format(pasien))
    elif noRekamMed!=0:
        for x in listMedis:
            if x.get('IDRekam')==noRekamMed:
                hasilFilter.append(copy.deepcopy(x))        
    else:
        hasilFilter=copy.deepcopy(listMedis)

    for i in range(len(dataKolom['namaKolom'])):
        print('{}\t|'.format(dataKolom['namaKolom'][i]), end=' ')
    print('\n')
    for item in hasilFilter:
        for i in range(len(dataKolom['namaKolom'])):
            print('{}\t|'.format(item[dataKolom['namaKolom'][i]]), end=' ')
        print('\n')
    if len(hasilFilter)<=0:
        print('\nRekam medis tidak ditemukan, cek kembali pencarian Anda')
    print('\n')
    return hasilFilter

def cariEntri():
    while True:
        tipeCari=input('''
Cari rekam medis
1. Tampilkan semua rekam medis
2. Tampilkan rekam medis pasien tertentu
3. Tampilkan rekam medis berdasarkan penyakit
                           
0. Kembali ke menu utama
Masukkan opsi yang diinginkan : ''')
    
        if tipeCari=='0':
            keluar=input('Yakin ingin keluar? (y/n) : ')
            if keluar=='y':
                break
        elif tipeCari=='1':
            tampilEntri()
        elif tipeCari=='2':
            while True:
                try:
                    nomorPasien=int(input('Masukkan ID Pasien :'))
                    if (nomorPasien==0):
                        print('Nomor pasien yang dimasukkan tidak valid')
                    else:
                        break
                except ValueError:
                    print('Nomor pasien yang dimasukkan tidak valid')
            tampilEntri(pasien=nomorPasien)
        elif tipeCari=='3':
            namaDiagnosa=input('Masukkan diagnosa yang dicari :')
            tampilEntri(penyakit=namaDiagnosa)
        else:
            print('Masukkan opsi yang valid!')

def inputEntri():
    while True:
        
        tipeCari=input('''
Tambah rekam medis baru
1. Tambah rekam medis baru
                           
0. Kembali ke menu utama
Masukkan opsi yang diinginkan : ''')
    
        if tipeCari=='0':
            keluar=input('Yakin ingin keluar? (y/n) : ')
            if keluar=='y':
                break
        
        elif tipeCari=='1':
            q=tampilEntri(noRekamMed=0)
            masukEntri(q)
        else:
            print('Masukkan opsi yang valid!')

def hapusEntri():
    while True:
        tipeCari=input('''
Hapus rekam medis
1. Hapus rekam medis tertentu
2. Hapus semua rekam medis pasien                     
                           
0. Kembali ke menu utama
Masukkan opsi yang diinginkan : ''')
    
        if tipeCari=='0':
            keluar=input('Yakin ingin keluar? (y/n) : ')
            if keluar=='y':
                break
        elif tipeCari=='1':
            while True:
                try:
                    idRekam=int(input('\nTekan 0 untuk kembali ke menu hapus\nMasukkan nomor rekam medis :'))
                    if idRekam==0:
                        del idRekam
                        break
                    q=tampilEntri(noRekamMed=idRekam)
                    if len(q)<=0:
                        del idRekam
                        break
                    elif int(idRekam)>0:

                        konfirmHapus=input('Yakin ingin hapus rekam medis nomor {}? (y/n) : '.format(idRekam))
                        if konfirmHapus=='y':
                            for item in q:
                                rekamMedis.remove(item)
                            print('Rekam medis sukses dihapus')
                        break
                except ValueError:
                    print('Masukkan angka yang valid!')
        elif tipeCari=='2':
            while True:
                try:
                    idPasien=int(input('\nTekan 0 untuk kembali ke menu hapus\nMasukkan nomor pasien :'))
                    if idPasien==0:
                        del idPasien
                        break
                    q=tampilEntri(pasien=idPasien)
                    if len(q)<=0:
                        del idPasien
                        break
                    elif int(idPasien)>0:

                        konfirmHapus=input('Yakin ingin hapus semua rekam medis pasien {}? (y/n) : '.format(q[0]['Nama']))
                        if konfirmHapus=='y':
                            for item in q:
                                rekamMedis.remove(item)
                            print('Rekam medis sukses dihapus')
                            break
                except ValueError:
                    print('Masukkan angka yang valid!')
        else:
            print('Masukkan opsi yang valid!')

def menuUbahEntri():
    while True:
        tipeCari=input('''
Ubah data rekam medis
1. Ubah data rekam medis tertentu                  
                           
0. Kembali ke menu utama
Masukkan opsi yang diinginkan : ''')
    
        if tipeCari=='0':
            keluar=input('Yakin ingin keluar? (y/n) : ')
            if keluar=='y':
                break
        elif tipeCari=='1':
            
            q=[]
            while len(q)<=0:
                try:
                    idRekam=int(input('\nTekan 0 untuk kembali ke menu ubah entri\nMasukkan nomor rekam medis:'))
                    q=tampilEntri(noRekamMed=idRekam)
                    if (idRekam==0 or len(q)<=0):
                        break

                    else:
                        
                        masukEntri(q,mode='Ubah')
                        
                except ValueError or idRekam==0:
                    print('Nomor rekam medis yang dimasukkan tidak valid')
            
            
        else:
            print('Masukkan opsi yang valid!')

def masukEntri(q,mode='baru'):
    if mode=='Ubah':
        r=copy.deepcopy(q)
        idRekam=r[0]['IDRekam']
        teks=['yang akan diubah','pengganti','mengubah']
    else:
        r=[{'IDRekam':'n/a'}]
        idRekam=r[0]['IDRekam']
        for  i in dataKolom['namaKolom']:
            r[0].update({i:'n/a'})
        teks=['baru','baru','menambahkan']
    while True:
        kolomUbah='n/a'
        if mode=='Ubah' or kolomUbah=='n/a':
            if len(q)<=0:
                break
            kolomUbah=input('Masukkan kolom data pasien {}: '.format(teks[0]))
        for i in range(len(dataKolom['namaKolom'])):
            if mode=='baru' and r[0][dataKolom['namaKolom'][i]]=='n/a':
                print('\nMohon isi dahulu kolom {}'.format(dataKolom['namaKolom'][i]))
                kolomUbah=copy.deepcopy(dataKolom['namaKolom'][i])
            
            if dataKolom['tipeKolom'][i]=='int' and dataKolom['namaKolom'][i]==kolomUbah:
                while True:
                    try:
                        data=int(input('Masukkan {} {}:'.format(dataKolom['namaKolom'][i],teks[1])))
                        
                        if (data==0):
                            print('Nomor {} yang dimasukkan tidak valid'.format(dataKolom['namaKolom'][i]))
                            continue
                        if kolomUbah=='IDRekam':
                            for i in range(len(rekamMedis)):
                                while (data==rekamMedis[i]['IDRekam']):
                                    try:
                                        print('Sudah ada rekam medis dengan nomor id {}'.format(data))
                                        data=int(input('Masukkan {} {}:'.format(dataKolom['namaKolom'][i],teks[1])))
                                        r[0].update({'IDRekam':data})
                                        break
                                    except ValueError:
                                        print('Nomor {} yang dimasukkan tidak valid'.format(dataKolom['namaKolom'][i]))
                                        
                                else:
                                    r[0].update({dataKolom['namaKolom'][i]:data})
                                    idRekam=copy.deepcopy(data)
                        else:
                            r[0].update({dataKolom['namaKolom'][i]:data})
                        
                        break
                    except ValueError:
                        print('Nomor yang dimasukkan tidak valid')
            elif dataKolom['tipeKolom'][i]=='str' and dataKolom['namaKolom'][i]==kolomUbah:
                data=input('Masukkan {}:'.format(dataKolom['namaKolom'][i]))
                r[0].update({dataKolom['namaKolom'][i]:data})
            elif dataKolom['tipeKolom'][i]=='date' and dataKolom['namaKolom'][i]==kolomUbah:
                
                while True:
                    try:
                        data=input('Masukkan {} dalam format DD-MM-YYYY:'.format(dataKolom['namaKolom'][i]))
                        day, month, year=map(int,data.split('-'))
                        tgl=datetime.date(year,month,day)
                        break
                    except ValueError:
                        print('Masukkan tanggal yang valid!')
                r[0].update({dataKolom['namaKolom'][i]:tgl})
                                
        tambahKolom=input('Apakah ingin memasukkan kolom lainnya? (y/n) : ')
        if tambahKolom=='n':

            break

    # tampilEntri(listMedis=r,noRekamMed=idRekam)
    tampilEntri(listMedis=r)
    konfirmUbah=input('Yakin ingin {} rekam medis nomor {}? (y/n) : '.format(teks[2],idRekam))
    if konfirmUbah=='y':
        if mode=='Ubah':
            for item in q:
                rekamMedis.remove(item)
        for item in r:
            rekamMedis.append(item)
        print('Rekam medis sukses disimpan')
        return r
    

def janjiTemu():
    
    
    while True:
        try:
            opsi=input('''
1. Jadwalkan janji temu dengan pasien baru
2. Jadwalkan janji temu untuk pasien lama
              
0. Kembali ke menu utama
Masukkan opsi yang diinginkan :''')
            
            if opsi=='1':
                q=tampilEntri(noRekamMed=0)
                q=masukEntri(q)
                if q is None:
                    continue
                rekamMedisTerpilih=q[0]['IDRekam']
            elif opsi=='2':
                rekamMedisTerpilih=int(input('Masukkan nomor rekam medis:'))
                if rekamMedisTerpilih==0:
                    print('Nomor rekam medis yang dimasukkan tidak valid')
                    continue
                q=tampilEntri(noRekamMed=rekamMedisTerpilih)
                if q is None:
                    continue
            else:
                keluar=input('Yakin ingin keluar? (y/n) : ')
                if keluar=='y':
                    break
                continue
            
            if len(q)>0:
                while True:
                    try:
                        jumlahKunjungan=int(input('Jumlah janji temu yang akan dijadwalkan: '))
                        intervalKunjungan=int(input('Interval janji temu yang diinginkan: '))
                        break
                    except ValueError or jumlahKunjungan<=0:
                        print('Jumlah yang dimaksudkan tidak valid')
                r=[]
                r.append(copy.deepcopy(q[0])) 
                for i in range(1,jumlahKunjungan+1):
                    r.append(copy.deepcopy(r[i-1]))
                    r[i].update({'IDRekam':r[i-1].get('IDRekam')+1})
                    r[i].update({'Tanggal':r[i-1].get('Tanggal')+datetime.timedelta(days=intervalKunjungan)})                           
                    for j in range(len(rekamMedis)):
                        if (r[i]['IDRekam']==rekamMedis[j]['IDRekam']):
                            r[i].update({'IDRekam':r[i].get('IDRekam')+1})
                        if (r[i]['Tanggal']==rekamMedis[j]['Tanggal'] and r[i]['Dokter']==rekamMedis[j]['Dokter']):
                            r[i].update({'Tanggal':r[i].get('Tanggal')+datetime.timedelta(days=1)})
                    
                tampilEntri(listMedis=r)
                konfirmUbah=input('Yakin ingin menjadwalkan janji temu untuk rekam medis {}? (y/n) : '.format(rekamMedisTerpilih))
                if konfirmUbah=='y':
                    for item in q:
                        rekamMedis.remove(item)                   
                    for item in r:
                        rekamMedis.append(item)
                    print('Rekam medis sukses disimpan')

            continue
        except ValueError:
            print('Nomor rekam medis yang dimasukkan tidak valid')

def opsiProgram():
    while True:
        opsi=input(

'''Selamat datang di SistemInfo Pasien 1.0
        
1. Cari rekam medis pasien
2. Input rekam medis baru
3. Hapus rekam medis 
4. Ubah rekam medis 
5. Jadwalkan janji temu

0. Keluar dari program
Masukkan opsi yang diinginkan: '''
    )

        if opsi=='0':
            keluar=input('Yakin ingin keluar? (y/n) : ')
            if keluar=='y':
                break

        elif opsi=='1':
            cariEntri()

        elif opsi=='2':
            inputEntri()

        elif opsi=='3':
            hapusEntri()

        elif opsi=='4':
            menuUbahEntri()  
        
        elif opsi=='5':
            janjiTemu()  

        else:
            print('Masukkan opsi yang valid!')


opsiProgram()

    


