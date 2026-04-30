import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# =============================================
# LOAD DATA
# =============================================

@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "main_data.csv")
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Mapping label agar lebih mudah dibaca di filter
    season_map = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
    df['season_label'] = df['season'].map(season_map)
    
    workingday_map = {0: 'Hari Libur', 1: 'Hari Kerja'}
    df['workingday_label'] = df['workingday'].map(workingday_map)
    
    return df

main_data = load_data()

# =============================================
# SIDEBAR (FITUR INTERAKTIF)
# =============================================

st.sidebar.title("Filter Data")

# 1. Filter Rentang Tanggal
min_date = main_data["dteday"].min()
max_date = main_data["dteday"].max()

start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# 2. Filter Musim
season_list = main_data['season_label'].unique()
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim:",
    options=season_list,
    default=season_list
)

# Menerapkan Filter ke Data
main_filtered = main_data[
    (main_data["dteday"] >= pd.to_datetime(start_date)) & 
    (main_data["dteday"] <= pd.to_datetime(end_date)) &
    (main_data["season_label"].isin(selected_seasons))
]

# Memisahkan kembali source data setelah difilter
df_day_clean = main_filtered[main_filtered['source'] == 'day']
df_hour_clean = main_filtered[main_filtered['source'] == 'hour']

# =============================================
# DASHBOARD
# =============================================

st.title('🚲 Dashboard Analisis Bike Sharing')
st.markdown(f"Menampilkan data dari **{start_date}** hingga **{end_date}**")

# --- VISUALISASI PERTANYAAN 1 ---

st.subheader('Total Peminjaman Sepeda pada Hari Kerja vs Hari Libur')

# Plotting Pertanyaan 1
fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df_day_clean, x='workingday_label', y='cnt', estimator=sum, errorbar=None, palette='Set2', ax=axes1[0])
axes1[0].set_title('Harian')
axes1[0].set_xlabel('Jenis Hari')
axes1[0].set_ylabel('Total Peminjaman')

sns.barplot(data=df_hour_clean, x='workingday_label', y='cnt', estimator=sum, errorbar=None, palette='Set2', ax=axes1[1])
axes1[1].set_title('Per Jam')
axes1[1].set_xlabel('Jenis Hari')
axes1[1].set_ylabel('Total Peminjaman')

plt.tight_layout()
st.pyplot(fig1)


# --- VISUALISASI PERTANYAAN 2 ---

st.subheader('Total Peminjaman Sepeda per Musim')

# Plotting Pertanyaan 2
# Seperti pada image_e4dd40.png dan image_e4dd39.png, kita menggunakan warna berbeda tiap musim
fig2, axes2 = plt.subplots(1, 2, figsize=(12, 5))

sns.barplot(data=df_day_clean, x='season_label', y='cnt', estimator=sum, errorbar=None, palette='viridis', ax=axes2[0])
axes2[0].set_title('Harian')
axes2[0].set_xlabel('Musim')
axes2[0].set_ylabel('Total Peminjaman')

sns.barplot(data=df_hour_clean, x='season_label', y='cnt', estimator=sum, errorbar=None, palette='viridis', ax=axes2[1])
axes2[1].set_title('Per Jam')
axes2[1].set_xlabel('Musim')
axes2[1].set_ylabel('Total Peminjaman')

plt.tight_layout()
st.pyplot(fig2)

# Menambahkan metriks ringkasan di bawah sebagai pengganti tabel
col_m1, col_m2 = st.columns(2)
col_m1.metric("Total Peminjaman (Filter Terpilih)", f"{int(df_day_clean['cnt'].sum()):,}")
col_m2.metric("Rata-rata Peminjaman Harian", f"{int(df_day_clean['cnt'].mean()):,}" if not df_day_clean.empty else 0)
