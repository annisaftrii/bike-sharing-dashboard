# 🚲 Dashboard Analisis Bike Sharing

## Deskripsi

Dashboard interaktif untuk menganalisis data peminjaman sepeda tahun 2011–2012 menggunakan dataset Bike Sharing. Dashboard ini menjawab pertanyaan bisnis seputar pola peminjaman berdasarkan hari kerja vs hari libur serta tren musiman.

## Pertanyaan Bisnis

1. Berapa total dan rata-rata peminjaman sepeda pada **hari kerja** dibandingkan **hari libur** sepanjang tahun 2011–2012 untuk menentukan strategi pengelolaan armada sepeda?
2. Pada **musim** apa jumlah total peminjaman sepeda paling tinggi dan paling rendah sepanjang tahun 2011–2012 untuk menentukan strategi promosi dan pemeliharaan armada?

## Struktur Proyek

```
bike-sharing-dashboard/
├── Submission Belajar Fundamental Analisis Data/
│   ├── dashboard/
│   │   ├── dashboard.py
│   │   └── main_data.csv
│   ├── data/
│   ├── notebook.ipynb
│   ├── url.txt
│   └── requirements.txt
└── README.md
```

## Setup Environment

### Prasyarat

Pastikan kamu sudah menginstal:

- [Python](https://www.python.org/downloads/) versi **3.8** atau lebih baru
- [pip](https://pip.pypa.io/en/stable/) (biasanya sudah termasuk saat instalasi Python)

### 1. Clone Repositori

```bash
git clone https://github.com/annisaftrii/bike-sharing-dashboard.git
cd bike-sharing-dashboard
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan Dashboard

```bash
streamlit run dashboard/dashboard.py
```

Setelah perintah dijalankan, dashboard akan otomatis terbuka di browser pada alamat:

```
http://localhost:8501
```

## Requirements

Berikut library yang digunakan (lihat `requirements.txt`):

| Library      | Kegunaan                            |
|--------------|-------------------------------------|
| streamlit    | Framework dashboard interaktif      |
| pandas       | Pengolahan dan analisis data        |
| matplotlib   | Visualisasi data                    |
| seaborn      | Visualisasi statistik               |
| numpy        | Komputasi numerik                   |

## Sumber Data

Dataset yang digunakan adalah **Bike Sharing Dataset** yang tersedia di [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset).
