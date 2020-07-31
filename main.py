#Percabangan
is_fast = True

if is_fast:
    print('fast route')
else:
    print('slow route')

#perulangan
jumlah_anak = 4

for index in range(1, jumlah_anak+1):
    print(f'Halo anak ke {index}')

#tipe data list
anak = ['eko', 'dhani', 'kay', 'donna']
print(anak)
anak.append('gita')
print(anak)

#perulangan list
for a in anak:
    print(f'Hi {a}')

#perulangan cara 2
for a in range(0, len(anak)):
    print(f'{a+1}. Hi {anak[a]}')
