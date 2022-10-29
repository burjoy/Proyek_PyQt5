# Schedule planner for control laboratory using “gspread” API
Proyek pembuatan GUI dengan python melalui interface PyQT5 dalam rangka pencaslaban kendali 2022

Required Module
  - PyQT5
  - Numpy
  - Gspread

Terdapat 3 buah laman navigasi pada program yaitu Landing Page, Laman Praktikan, dan Laman Aslab.
Tata Cara Penggunaan 
  1. Run Program Landing_Page.py untuk membuka laman landing Page
  2. Jika ingin masuk sebagai praktikan, tekan tombol praktikan. 
  3. Jika ingin masuk sebagai Aslab, masukan password "password123" lalu tekan tombol login
  4. Silahkan gunakan program sesuai dengan identitas yang digunakan
 
 Fitur yang terdapat pada program antara lain
 
  **Sebagai Aslab**
    - Input Sesi Aslab (Tanggal, Waktu Sesi, Kode Aslab)
    - Error Handling apabila sesi telah digunakan
    - Terkoneksi dengan google sheet pengambilan jadwal
  
  
  **Sebagai Praktikan**
    - Input Sesi Praktikan (Tanggal, Waktu Sesi, Kode Aslab)
    - Counter urutan praktikan untuk mengambil jadwal
    - Terkoneksi dengan google sheet pengambilan jadwal
    - Error handling apabila sesi telah diisi
