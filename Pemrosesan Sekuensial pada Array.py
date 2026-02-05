# Pemrosesan Sekuensial pada Array latihan
var_arr = [1,2,3,4,5]
for i in range(len(var_arr)):
    elemen_sekarang = var_arr[i]
    element_selanjutnya = i+1
    if element_selanjutnya < len(var_arr):
        element_selanjutnya = var_arr[element_selanjutnya]
    else:
        element_selanjutnya=None

    print(f"element saat ini nya: {elemen_sekarang}, element berikutnya {element_selanjutnya}")