data_panen = {
    'lokasi' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    }, 
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 950,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    },     
}

for panen in data_panen:
    print(f"{panen}: {data_panen[panen]}")
    
print(f"Jumlah hasil panen jagung dari lokasi2:", data_panen['lokasi2']['hasil_panen']['jagung'])
print(f"Nama lokasi3:", data_panen['lokasi3']['nama_lokasi'])

for data in data_panen:
    padi = data_panen[data]['hasil_panen']['padi']
    kedelai = data_panen[data]['hasil_panen']['kedelai']
    jagung = data_panen[data]['hasil_panen']['jagung']
    
    if padi > 1300 or jagung < 800:
        print(f"{data_panen[data]['hasil_panen']} memerlukan perhatian khusus")
    else:
        print("lokasi dalam kondisi baik")