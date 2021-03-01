# MKPlanner
MKPlanner merupakan program python sederhana yang tugasnya menyusun rencana kuliah berdasarkan data mata kuliah dan prasyaratnya dengan menggunakan topological sort yang memanfaatkan algoritma Decrease and Conquer

# Algoritma
Algoritma decrease and conquer: 
1.	Hitung derajat masuk setiap simpul pada graf (N).
2.	Eliminasi n simpul dengan derajat = 0 dan simpan simpul tersebut pada sebuah tuple solusi. Untuk setiap simpul yang dieliminasi, lakukan pengurangan derajat masuk dari simpul yang bersisian dari simpul yang dieliminasi (next node )
3.	Ulangi proses 1-2 terhadap N-n simpul yang tersisa.

# Cara Penggunaan
1. Buka cmd
2. pindahkan cd ke lokasi mainprog.py
3. Run mainprog.py dengan mengetik "Python3 mainprog.py"
4. Masukkan nama file pada saat muncul pesan "Enter filename : ". Pastikan file terdapat pada folder test dan format isi file sesuai dengan berikut.

 <kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, <kode kuliah prasyarat - 3>.

5. Rencana Kuliah akan ditampilkan pada layar

# Batasan 
program ini hanya akan menampilkan rencana kuliah untuk maksimal 8 semester

# AUTHOR
13519045 - M.Reyhanullah Budiaman
