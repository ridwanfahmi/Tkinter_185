import tkinter as tk  # Mengimpor modul tkinter sebagai 'tk' untuk membuat antarmuka GUI

def show_prediction():
    # Mengatur teks label 'prediction_label' untuk menampilkan hasil prediksi
    prediction_label.config(text="Prediksi: Teknologi Informasi")

# Inisialisasi jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela utama aplikasi
root.geometry("400x500")  # Mengatur ukuran jendela utama menjadi lebar 400 piksel dan tinggi 500 piksel

# Membuat label judul untuk aplikasi
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label dengan teks dan ukuran font
title_label.pack(pady=10)  # Menempatkan label di jendela utama dengan jarak vertikal 10 piksel dari elemen lain

# Membuat frame untuk menampung input nilai mata pelajaran
input_frame = tk.Frame(root)  # Membuat frame di dalam jendela utama untuk mengelompokkan input
input_frame.pack(pady=10)  # Menempatkan frame di jendela utama dengan jarak vertikal 10 piksel

# Membuat kolom input untuk nilai dari 10 mata pelajaran
entries = []  # List untuk menyimpan referensi ke setiap kolom input
for i in range(1, 11):  # Loop untuk membuat 10 kolom input
    # Membuat label untuk setiap mata pelajaran
    subject_label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i}:")
    subject_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")  # Menempatkan label di grid, kolom pertama, dengan jarak horizontal 10 piksel
    
    # Membuat kolom input untuk nilai mata pelajaran
    entry = tk.Entry(input_frame, width=10)  # Membuat kolom input dengan lebar 10 karakter
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan kolom input di grid, kolom kedua, di samping label
    entries.append(entry)  # Menyimpan kolom input di list 'entries' untuk referensi nanti

# Membuat tombol prediksi untuk menampilkan hasil prediksi
predict_button = tk.Button(root, text="Hasil Prediksi", command=show_prediction)  # Membuat tombol dengan teks "Hasil Prediksi"
predict_button.pack(pady=10)  # Menempatkan tombol di bawah frame input dengan jarak vertikal 10 piksel

# Membuat label untuk menampilkan hasil prediksi
prediction_label = tk.Label(root, text="Prediksi: ", font=("Arial", 12), fg="black")  # Membuat label dengan teks awal dan warna biru
prediction_label.pack(pady=20)  # Menempatkan label di bawah tombol dengan jarak vertikal 20 piksel

# Menjalankan aplikasi GUI
root.mainloop()  # Memulai loop utama tkinter untuk menampilkan dan menjaga GUI tetap aktif
