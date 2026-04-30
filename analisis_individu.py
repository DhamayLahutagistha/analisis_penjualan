import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import os

# 1. Alamat File (Pastikan sesuai dengan lokasi running di terminal)
csv_path = 'Analisis Penjualan/women_clothing_ecommerce_sales.csv'

# Jika error "File not found", aktifkan baris di bawah ini untuk auto-path:
# csv_path = os.path.join(os.path.dirname(__file__), 'women_clothing_ecommerce_sales.csv')

print("--- Memulai Analisis Sesuai Modul Praktikum ---")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    
    # --- AUTO DETECT KOLOM ---
    cols = df.columns.tolist()
    date_col = next((c for c in cols if 'date' in c.lower()), None)
    price_col = next((c for c in cols if 'price' in c.lower()), None)
    qty_col = next((c for c in cols if 'quant' in c.lower() or 'qty' in c.lower()), None)
    user_col = next((c for c in cols if 'customer' in c.lower() or 'id' in c.lower()), None)

    if not all([date_col, price_col, qty_col]):
        print(f"Error: Kolom tidak lengkap. Ditemukan: {cols}")
    else:
        # 2. Data Wrangling
        df = df.dropna(subset=[date_col, price_col])
        df[date_col] = pd.to_datetime(df[date_col])
        df = df[df[price_col] > 0]
        df['Total_Sales'] = df[qty_col] * df[price_col]

        # 3. Visualisasi Tren
        df['Month'] = df[date_col].dt.to_period('M').astype(str)
        monthly_sales = df.groupby('Month')['Total_Sales'].sum()

        plt.figure(figsize=(10, 5))
        monthly_sales.plot(kind='line', marker='o', color='teal')
        plt.title('Tren Penjualan Bulanan')
        plt.grid(True, alpha=0.3)
        plt.show()

        # 4. RFM Analysis (FIXED VERSION)
        print("\n--- Menghitung RFM Analysis ---")
        snapshot_date = df[date_col].max() + dt.timedelta(days=1)
        
        # Menggunakan .agg dengan cara yang lebih aman untuk penamaan kolom
        rfm = df.groupby(user_col if user_col else df.index).agg({
            date_col: [lambda x: (snapshot_date - x.max()).days, 'count'],
            'Total_Sales': 'sum'
        })
        
        # Meratakan kolom dan memberi nama baru
        rfm.columns = ['Recency', 'Frequency', 'Monetary']
        rfm = rfm.reset_index()
        print(rfm.head())

        # 5. Heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(df[[qty_col, price_col, 'Total_Sales']].corr(), annot=True, cmap='coolwarm')
        plt.title('Peta Korelasi')
        plt.show()

        # RINGKASAN
        print("\n" + "="*40)
        print("INSIGHT UNTUK LAPORAN:")
        print(f"1. Puncak Penjualan: {monthly_sales.idxmax()}")
        print(f"2. Total Pelanggan Unik: {rfm.iloc[:,0].nunique()}")
        print(f"3. Rekomendasi: Fokus pada bulan {monthly_sales.idxmin()} dengan promo.")
        print("="*40)
else:
    print(f"File TIDAK DITEMUKAN di: {os.path.abspath(csv_path)}")