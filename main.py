# Percabangan
is_fast = True

if is_fast:
    print('fast route')
else:
    print('slow route')

# perulangan
jumlah_anak = 4

for index in range(1, jumlah_anak + 1):
    print(f'Halo anak ke {index}')

# tipe data list
anak = ['eko', 'dhani', 'kay', 'donna']
print(anak)
anak.append('gita')
print(anak)

# perulangan list
for a in anak:
    print(f'Hi {a}')

# perulangan cara 2
for a in range(0, len(anak)):
    print(f'{a + 1}. Hi {anak[a]}')

print("-" * 20)
print("\n")

# tipe data json
data_driver = {
    'tanggal': '2020-08-12',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Djoko', 'jarak': 40},
        {'nama': 'Dwi', 'jarak': 120},
        {'nama': 'Dhani', 'jarak': 240},
    ]
}

try:
    print(f"Driver terdekat berjarak {data_driver['driver_list'][2]['jarak']} meter")
except Exception as err:
    print('Error message : ', err)

print("-" * 20)
print("\n")

# mendefinisikan fungsi
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}")

hitung_luas_segitiga(10, 6)