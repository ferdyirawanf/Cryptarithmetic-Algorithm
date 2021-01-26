import time
import os

curent_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\test\\input1.txt', curent_path)

def buka_file():
    with open(new_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def buka_file2():
    with open(new_path, 'r') as file2:
        my_list = list(file2)
    return my_list

def hitung_baris():
    file = open(new_path, 'r')
    jumlah_baris = 0
    for line in file:
        if line != "\n":
            jumlah_baris += 1
    return jumlah_baris

def panjang_string(string):
    panjang = 0
    for char in string:
        panjang = panjang + 1
    return panjang

def panjang_list(mylist):
    panjang = 0
    for x in mylist:
        panjang = panjang + 1
    return panjang

def string_unik(mylist,string_operan):
    list_unik = []
    for i in range(0,panjang_string(string_operan)):
        j = 0
        huruf_sama = False
        while (j < panjang_list(list_unik) and huruf_sama == False):
            if (list_unik[j] == mylist[i]):
                huruf_sama = True
            j = j + 1
        if (huruf_sama == False and mylist[i] != '-' and mylist[i] != ' ' and mylist[i] != '+'):
            list_unik = list_unik + [mylist[i]]
    return list_unik

def permutasi(angka, panjang):
    list_hasil = []
    list_angka = list(angka)
    n = panjang_list(list_angka)
    putaran = list(range(n,n-panjang,-1))
    indeks = list(range(n))
    list_hasil += [list(list_angka[i] for i in indeks[:panjang])]
    while n:
        for i in range(panjang-1,-1,-1):
            putaran[i] = putaran[i] - 1
            if putaran[i] != 0:
                j = putaran[i]
                indeks[i], indeks[-j] = indeks[-j], indeks[i]
                list_hasil += [list(list_angka[i] for i in indeks[:panjang])]
                break
            else:
                indeks[i:] = indeks[i + 1:] + indeks[i:i + 1]
                putaran[i] = n - i
        else:
            return list_hasil

def ubah_desimal(list_string):
    desimal = 0
    for i in range(0,panjang_list(list_string)):
        desimal = desimal + list_string[i]*(10**(panjang_list(list_string)-i-1))
    return desimal

def operan(mylist):
    list_operan = []
    for i in range(0,panjang_list(mylist)):
        list_copy = [x for x in operan_hasil[i]]
        list_temp = []
        for j in range(0,panjang_list(list_copy)):
            if (list_copy[j] != '-' and list_copy[j] != '+' and list_copy[j] != '\n' and list_copy[j] != ' '):
                list_temp = list_temp + [list_copy[j]]
        list_operan = list_operan + [list_temp]
    return list_operan

def digit_maksimum(mylist):
    max = 0
    for i in range(0,panjang_list(mylist)):
        if max < panjang_string(mylist[i]):
            max = panjang_string(mylist[i])
    return max

def print_soal():
    print("Soal")
    with open(new_path, 'r') as file:
        data = file.read()
    print(data, '\n')

def print_jawaban(mylist,mylist2):
    print("Jawaban")
    if panjang_list(mylist) == 0:
        print("Tidak ada solusi yang memenuhi")
    else:
        print("Ada", panjang_list(mylist), "solusi yaitu:")
        maksimum = digit_maksimum(list_operan_hasil)
        for i in range(0,panjang_list(mylist)):
            print("Solusi ke-" + str(i+1))
            for j in range(0,panjang_list(mylist2[i])-3):
                selisih = maksimum - panjang_list(list_operan_hasil[j])
                if panjang_list(list_operan_hasil[j]) < maksimum:
                    for k in range(0,selisih+1):
                        print(' ', end='')
                    print(str(mylist2[i][j]))
                else:
                    print(' ' + str(mylist2[i][j]))

            print("+", end='')
            selisih2 = maksimum - panjang_list(list_operan_hasil[panjang_list(mylist2[i])-3])
            if panjang_list(list_operan_hasil[panjang_list(mylist2[i])-3]) < maksimum:
                for l in range(0, selisih2):
                    print(' ', end='')
                print(str(mylist2[i][panjang_list(mylist2[i])-3]))
            else:
                print(str(mylist2[i][panjang_list(mylist2[i])-3]))

            for m in range(0,maksimum+1):
                print('-', end='')
                if m == maksimum:
                    print('\n', end='')

            selisih3 = maksimum - panjang_list(list_operan_hasil[panjang_list(mylist2[i]) - 1])
            if panjang_list(list_operan_hasil[panjang_list(mylist2[i]) - 1]) < maksimum:
                for l in range(0, selisih3+1):
                    print(' ', end='')
                print(str(mylist2[i][panjang_list(mylist2[i]) - 1]))
            else:
                print(' ' + str(mylist2[i][panjang_list(mylist2[i]) - 1]))

# Main Program
input_sebaris = buka_file()
operan_hasil = buka_file2()

start = time.time()
list_input_sebaris = [x for x in input_sebaris]
list_string_unik = string_unik(list_input_sebaris,input_sebaris)

list_permutasi = permutasi([0,1,2,3,4,5,6,7,8,9],panjang_list(list_string_unik))

list_operan_hasil = operan(operan_hasil)

list_copy = []
for i in range(0,panjang_list(list_operan_hasil)):
    dummy = []
    for j in range(0,panjang_list(list_operan_hasil[i])):
        dummy = dummy + [list_operan_hasil[i][j]]
    list_copy = list_copy + [dummy]

list_solusi = []
list_solusi2 = []
for i in range(0,panjang_list(list_permutasi)):
    for j in range(0,panjang_list(list_string_unik)):
        for k in range(0,panjang_list(list_copy)):
            for l in range(0,panjang_list(list_copy[k])):
                if list_string_unik[j] == list_operan_hasil[k][l]:
                    list_copy[k][l] = list_permutasi[i][j]

    list_desimal = []
    for m in range(0, panjang_list(list_copy)):
        list_desimal = list_desimal + [ubah_desimal(list_copy[m])]
    hasil = 0
    for n in range(0, panjang_list(list_desimal)-2):
        hasil = hasil + list_desimal[n]
    temu = False
    for o in range(0,panjang_list(list_copy)-2):
        if list_copy[o][0] == 0:
            temu = True
    if hasil == list_desimal[panjang_list(list_desimal) - 1] and temu == False and list_copy[panjang_list(list_copy)-1][0] != 0:
        list_solusi = list_solusi + [list_permutasi[i]]
        list_solusi2 = list_solusi2 + [list_desimal]

print_soal()
print_jawaban(list_solusi,list_solusi2)
print("\nJumlah total tes adalah", panjang_list(list_permutasi), "kali substitusi atau permutasi")
end = time.time()
print("\nWaktu yang dibutuhkan adalah", end - start, "detik")
