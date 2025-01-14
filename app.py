# Import library yang dibutuhkan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data CSV
data = pd.read_csv('Regression.csv')

# Menambahkan CSS untuk memusatkan konten
st.markdown(
    """
    <style>
    .main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title('Dashboard Data Asuransi')

# Sidebar untuk filter
st.sidebar.header('Filter Data')

# Filter berdasarkan umur
age_filter = st.sidebar.slider(
    'Umur', 
    int(data['age'].min()), 
    int(data['age'].max()), 
    (int(data['age'].min()), int(data['age'].max()))
)
data = data[(data['age'] >= age_filter[0]) & (data['age'] <= age_filter[1])]

# Filter berdasarkan wilayah
region_filter = st.sidebar.multiselect('Wilayah', data['region'].unique(), data['region'].unique())
data = data[data['region'].isin(region_filter)]

# Filter berdasarkan jenis kelamin
sex_filter = st.sidebar.multiselect('Jenis Kelamin', data['sex'].unique(), data['sex'].unique())
data = data[data['sex'].isin(sex_filter)]

# Filter berdasarkan BMI
bmi_filter = st.sidebar.slider(
    'BMI', 
    float(data['bmi'].min()), 
    float(data['bmi'].max()), 
    (float(data['bmi'].min()), float(data['bmi'].max()))
)
data = data[(data['bmi'] >= bmi_filter[0]) & (data['bmi'] <= bmi_filter[1])]

# Filter berdasarkan status perokok
smoker_filter = st.sidebar.multiselect('Status Perokok', data['smoker'].unique(), data['smoker'].unique())
data = data[data['smoker'].isin(smoker_filter)]

# Filter berdasarkan biaya asuransi
charges_filter = st.sidebar.slider(
    'Biaya Asuransi', 
    float(data['charges'].min()), 
    float(data['charges'].max()), 
    (float(data['charges'].min()), float(data['charges'].max()))
)
data = data[(data['charges'] >= charges_filter[0]) & (data['charges'] <= charges_filter[1])]

# Menampilkan tabel data
st.header('Tabel Data')
st.dataframe(data)

# Pie chart: Distribusi jenis kelamin
st.header('Distribusi Jenis Kelamin')
sex_counts = data['sex'].value_counts()
fig1, ax1 = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax1.pie(
    sex_counts, 
    labels=sex_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff9999', '#66b3ff'], 
    textprops=dict(color="w")
)
ax1.axis('equal')
plt.setp(autotexts, size=10, weight="bold")
ax1.set_title("Distribusi Jenis Kelamin", color='#333333', fontsize=14)
st.pyplot(fig1)

# Pie chart: Distribusi status perokok
st.header('Distribusi Status Perokok')
smoker_counts = data['smoker'].value_counts()
fig2, ax2 = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax2.pie(
    smoker_counts, 
    labels=smoker_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#99ff99', '#ffcc99'], 
    textprops=dict(color="w")
)
ax2.axis('equal')
plt.setp(autotexts, size=10, weight="bold")
ax2.set_title("Distribusi Status Perokok", color='#333333', fontsize=14)
st.pyplot(fig2)

# Diagram batang: Jumlah anak per wilayah
st.header('Jumlah Anak per Wilayah')
fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.barplot(
    x='region', 
    y='children', 
    data=data, 
    ci=None, 
    palette='Set2'
)
ax3.set_title('Rata-rata Jumlah Anak per Wilayah', fontsize=14, color='#333333')
ax3.set_xlabel('Wilayah', fontsize=12)
ax3.set_ylabel('Jumlah Anak', fontsize=12)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
st.pyplot(fig3)

# Menampilkan informasi statistik deskriptif
st.header('Statistik Deskriptif')
st.write(data.describe())
