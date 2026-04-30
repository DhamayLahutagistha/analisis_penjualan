📊 Laporan Praktikum: Analisis Performa Penjualan E-commerce
Nama: [Isi Nama Kamu]

Dataset: women_clothing_ecommerce_sales.csv

Status: ✅ Selesai (Analisis Individu)

🎯 1. Business Question
Analisis ini dirancang untuk menjawab tantangan bisnis utama berikut:

Tren Penjualan: Bagaimana fluktuasi pendapatan setiap bulannya dan kapan periode emas penjualan terjadi?

Segmentasi Pelanggan: Siapa pelanggan yang paling loyal dan berhak mendapatkan apresiasi berupa voucher?

Efisiensi Produk: Apakah ada produk dengan harga tinggi namun jarang laku (underperformer)?

Prediksi Penjualan: Sejauh mana variabel harga dapat memprediksi total nilai penjualan masa depan?

🛠️ 2. Data Wrangling
Proses cleaning dilakukan untuk memastikan data siap dianalisis tanpa adanya bias:

Pembersihan Data: Menghapus nilai kosong (null values) pada kolom krusial.

Filter Anomali: Menghapus transaksi dengan harga ≤ 0 yang dapat merusak rata-rata.

Transformasi Tipe Data: Mengonversi kolom tanggal menjadi format datetime untuk pengolahan runtun waktu.

Rekayasa Fitur: Menghitung Total_Sales sebagai hasil perkalian antara kuantitas dan harga satuan.

📈 3. Insights (Analisis & Visualisasi)
A. Tren Penjualan Bulanan
Visualisasi menggunakan Line Chart menunjukkan dinamika pendapatan.

Insight: Kita dapat mengidentifikasi bulan dengan performa tertinggi untuk menentukan kapan kampanye pemasaran harus dijalankan.

B. Segmentasi Pelanggan (RFM Analysis)
Pelanggan dikelompokkan berdasarkan perilaku transaksi nyata:

Recency: Kapan terakhir kali mereka belanja?

Frequency: Seberapa sering mereka kembali?

Monetary: Berapa total kontribusi finansial mereka?

Hasil: Pelanggan diberikan skor 1-5. Grup pelanggan dengan skor "555" adalah prioritas utama untuk program retensi.

C. Identifikasi Produk "Underperformer"
Melalui Scatter Plot, kami membandingkan Harga Satuan vs Jumlah Terjual.

Temuan: Produk di area harga tinggi namun volume rendah diidentifikasi sebagai produk yang membebani arus kas.

D. Analisis Prediktif (Regresi Linear)
Menggunakan model matematika untuk memprediksi total penjualan berdasarkan harga.

Output: Nilai R2 Score digunakan untuk mengukur seberapa akurat variabel harga dalam memprediksi penjualan.

💡 4. Recommendation
Berdasarkan hasil pengolahan data, berikut adalah rekomendasi strategisnya:

Retention Program: Berikan insentif eksklusif bagi segmen pelanggan "Loyal" (Skor RFM Tinggi).

Price Optimization: Lakukan tinjauan harga atau diskon khusus untuk produk underperformer agar stok lebih cepat bergerak.

Marketing Strategy: Tingkatkan anggaran iklan pada bulan-bulan menjelang puncak tren penjualan tahunan.

🗂️ 5. Teknologi yang Digunakan
Bahasa: Python 3.x

Library Utama: Pandas, Matplotlib, Seaborn, Scikit-Learn

Laporan ini disusun sebagai bagian dari pemenuhan tugas praktikum Analisis dan Visualisasi Data.

