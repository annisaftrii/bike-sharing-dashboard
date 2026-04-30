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
    
    # Mapping label hanya jika kolom berisi angka (menghindari hasil 'nan')
    if df['season'].dtype in [np.int64, np.float64]:
        season_map = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
        df['season'] = df['season'].map(season_map)
    
    if df['workingday'].dtype in [np.int64, np.float64]:
        workingday_map = {0: 'Hari Libur', 1: 'Hari Kerja'}
        df['workingday'] = df['workingday'].map(workingday_map)

    # Membersihkan baris kosong agar tidak muncul 'nan' di filter sidebar
    df = df.dropna(subset=['season', 'workingday'])
    
    return df

main_data = load_data()

# =============================================
# SIDEBAR (FITUR INTERAKTIF)
# =============================================

st.sidebar.title("Filter")

# Filter Rentang Tanggal
min_date = main_data["dteday"].min()
max_date = main_data["dteday"].max()

start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Filter Musim (Mengambil list unik yang sudah bersih dari nan)
season_options = main_data['season'].unique()

selected_seasons = st.sidebar.multiselect(
    "Pilih Musim:",
    options=season_options,
    default=season_options
)

# Logic Filtering
main_filtered = main_data[
    (main_data["dteday"] >= pd.to_datetime(start_date)) & 
    (main_data["dteday"] <= pd.to_datetime(end_date)) &
    (main_data["season"].isin(selected_seasons))
]

df_day_clean = main_filtered[main_filtered['source'] == 'day']
df_hour_clean = main_filtered[main_filtered['source'] == 'hour']

# =============================================
# DASHBOARD
# =============================================

st.title('🚲 Dashboard Analisis Bike Sharing')

# PERTANYAAN 1
st.subheader('Pertanyaan 1: Total Peminjaman Sepeda pada Hari Kerja vs Hari Libur (2011-2012)')

# Hanya tampilkan plot jika data hasil filter tersedia
if not df_day_clean.empty:
    fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))
    sns.barplot(data=df_day_clean, x='workingday', y='cnt', estimator=sum, errorbar=None, palette='Set2', ax=axes1[0])
    axes1[0].set_title('Harian')
    axes1[0].set_xlabel('Jenis Hari')
    axes1[0].set_ylabel('Total Peminjaman')

    sns.barplot(data=df_hour_clean, x='workingday', y='cnt', estimator=sum, errorbar=None, palette='Set2', ax=axes1[1])
    axes1[1].set_title('Per Jam')
    axes1[1].set_xlabel('Jenis Hari')
    axes1[1].set_ylabel('Total Peminjaman')

    plt.tight_layout()
    st.pyplot(fig1)

    # PERTANYAAN 2
    st.subheader('Pertanyaan 2: Total Peminjaman Sepeda per Musim (2011-2012)')

    fig2, axes2 = plt.subplots(1, 2, figsize=(12, 5))
    sns.barplot(data=df_day_clean, x='season', y='cnt', estimator=sum, errorbar=None, palette='Set1', ax=axes2[0])
    axes2[0].set_title('Harian')
    axes2[0].set_xlabel('Musim')
    axes2[0].set_ylabel('Total Peminjaman')

    sns.barplot(data=df_hour_clean, x='season', y='cnt', estimator=sum, errorbar=None, palette='Set1', ax=axes2[1])
    axes2[1].set_title('Per Jam')
    axes2[1].set_xlabel('Musim')
    axes2[1].set_ylabel('Total Peminjaman')

    plt.tight_layout()
    st.pyplot(fig2)
else:
    st.warning("Silakan pilih filter musim di sidebar untuk menampilkan data.")
