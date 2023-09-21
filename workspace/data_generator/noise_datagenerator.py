import pandas as pd
import numpy as np

# Jumlah baris data
n = 1000

# Fungsi untuk menghasilkan data kotor
def generate_noisy_data(column_data, noise_factor):
    noise = np.random.randint(1, noise_factor, size=len(column_data))
    return column_data + noise

# Nama Pelanggan (misalkan kita memiliki 10 nama pelanggan yang berulang)
names = ["Pelanggan" + str(i) for i in range(1, 11)]
name_column = np.random.choice(names, n)

# Jenis Transaksi (Deposit, Transfer, Tarik Tunai)
transaction_types = ["Deposit", "Transfer", "Tarik Tunai"]
transaction_column = np.random.choice(transaction_types, n)

# Jumlah Transaksi (dalam Rupiah, dengan beberapa data kotor/noise)
amount_column = generate_noisy_data(np.random.randint(500000, 50000000, n), 100000)

# Tanggal Transaksi (antara 2020-01-01 hingga 2022-12-31)
date_column = pd.date_range('2020-01-01', '2022-12-31', freq='D').to_numpy()
transaction_date_column = np.random.choice(date_column, n)

# Lokasi (misalkan kita memiliki 5 lokasi)
locations = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan"]
location_column = np.random.choice(locations, n)

# Buat DataFrame
df = pd.DataFrame({
    "Nama": name_column,
    "Jenis Transaksi": transaction_column,
    "Jumlah (Rp)": amount_column,
    "Tanggal Transaksi": transaction_date_column,
    "Lokasi": location_column
})

# Simpan dalam format CSV
df.to_csv("~/project/APUChat/workspace/data/noise_data.csv", index=False)
