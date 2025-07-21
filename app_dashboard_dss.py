# Simpan sebagai app_dashboard_dss.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data simulasi (pastikan file disimpan)
data = pd.read_excel("simulasi_data_penelitian_DSS.xlsx")

st.title("📊 Dashboard DSS Iklim: CT vs Literasi Iklim")

# Pilihan variabel
x_var = st.selectbox("Pilih Variabel CT", data.columns[:5])
y_var = st.selectbox("Pilih Variabel Literasi Iklim", data.columns[5:])

# Tampilkan grafik
st.subheader("Visualisasi Korelasi Regresi")
fig, ax = plt.subplots()
sns.regplot(x=x_var, y=y_var, data=data, ax=ax, scatter_kws={"alpha":0.6}, line_kws={"color":"red"})
st.pyplot(fig)

# Statistik Korelasi
corr = data[[x_var, y_var]].corr().iloc[0, 1]
st.write(f"**Nilai Korelasi (r):** {corr:.2f}")
