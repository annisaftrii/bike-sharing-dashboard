import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =============================================
# LOAD DATA
# =============================================

@st.cache_data
def load_data():
    df = pd.read_csv("Submission Belajar Fundamental Analisis Data/dashboard/main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_data = load_data()
df_day_clean = main_data[main_data['source'] == 'day'].copy()
df_hour_clean = main_data[main_data['source'] == 'hour'].copy()

# =============================================
# DASHBOARD
# =============================================

st.title('🚲 Dashboard Analisis Bike Sharing')
st.markdown('Analisis peminjaman sepeda tahun 2011-2012')

# =============================================
# PERTANYAAN 1
# =============================================

st.subheader('Pertanyaan 1: Total Peminjaman Sepeda pada Hari Kerja vs Hari Libur (2011-2012)')

hasil_1_day = df_day_clean.groupby('workingday')['cnt'].agg(['sum', 'mean', 'max', 'min']).round(2).reset_index()
hasil_1_day.columns = ['Jenis Hari', 'Total', 'Rata-rata', 'Maksimum', 'Minimum']

hasil_1_hour = df_hour_clean.groupby('workingday')['cnt'].agg(['sum', 'mean', 'max', 'min']).round(2).reset_index()
hasil_1_hour.columns = ['Jenis Hari', 'Total', 'Rata-rata', 'Maksimum', 'Minimum']

col1, col2 = st.columns(2)
with col1:
    st.markdown('**Data Harian**')
    st.dataframe(hasil_1_day)
with col2:
    st.markdown('**Data Per Jam**')
    st.dataframe(hasil_1_hour)

fig1, axes1 = plt.subplots(1, 2, figsize=(12, 5))
sns.barplot(data=hasil_1_day, x='Jenis Hari', y='Total', hue='Jenis Hari', palette='Set2', legend=False, ax=axes1[0])
axes1[0].set_title('Harian (2011-2012)')
axes1[0].set_xlabel('Jenis Hari')
axes1[0].set_ylabel('Total Peminjaman')
sns.barplot(data=hasil_1_hour, x='Jenis Hari', y='Total', hue='Jenis Hari', palette='Set2', legend=False, ax=axes1[1])
axes1[1].set_title('Per Jam (2011-2012)')
axes1[1].set_xlabel('Jenis Hari')
axes1[1].set_ylabel('Total Peminjaman')
fig1.suptitle('Total Peminjaman Sepeda: Hari Kerja vs Hari Libur', fontsize=14, fontweight='bold')
plt.tight_layout()
st.pyplot(fig1)

st.info('**Kesimpulan:** Hari Kerja memiliki total peminjaman lebih tinggi dibanding Hari Libur baik data harian maupun per jam. Sepeda lebih banyak digunakan untuk aktivitas rutin seperti bekerja atau sekolah.')

# =============================================
# PERTANYAAN 2
# =============================================

st.subheader('Pertanyaan 2: Total Peminjaman Sepeda per Musim (2011-2012)')

hasil_2_day = df_day_clean.groupby('season')['cnt'].agg(['sum', 'mean', 'max', 'min']).round(2).reset_index()
hasil_2_day.columns = ['Musim', 'Total', 'Rata-rata', 'Maksimum', 'Minimum']

hasil_2_hour = df_hour_clean.groupby('season')['cnt'].agg(['sum', 'mean', 'max', 'min']).round(2).reset_index()
hasil_2_hour.columns = ['Musim', 'Total', 'Rata-rata', 'Maksimum', 'Minimum']

col3, col4 = st.columns(2)
with col3:
    st.markdown('**Data Harian**')
    st.dataframe(hasil_2_day)
with col4:
    st.markdown('**Data Per Jam**')
    st.dataframe(hasil_2_hour)

fig2, axes2 = plt.subplots(1, 2, figsize=(12, 5))
sns.barplot(data=hasil_2_day, x='Musim', y='Total', hue='Musim', palette='Set1', legend=False, ax=axes2[0])
axes2[0].set_title('Harian (2011-2012)')
axes2[0].set_xlabel('Musim')
axes2[0].set_ylabel('Total Peminjaman')
sns.barplot(data=hasil_2_hour, x='Musim', y='Total', hue='Musim', palette='Set1', legend=False, ax=axes2[1])
axes2[1].set_title('Per Jam (2011-2012)')
axes2[1].set_xlabel('Musim')
axes2[1].set_ylabel('Total Peminjaman')
fig2.suptitle('Total Peminjaman Sepeda per Musim', fontsize=14, fontweight='bold')
plt.tight_layout()
st.pyplot(fig2)

st.info('**Kesimpulan:** Musim Gugur memiliki total peminjaman tertinggi dan Musim Semi terendah baik data harian maupun per jam. Kondisi cuaca di musim gugur lebih nyaman dan mendukung aktivitas bersepeda.')
