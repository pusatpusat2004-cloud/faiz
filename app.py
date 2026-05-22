import streamlit as st
import pandas as pd
import os

# Set judul halaman web
st.set_page_config(page_title="E-Raport RQIK", page_icon="📝", layout="centered")

st.title("📝 E-Raport RQIK - Input Nilai Tahfidz")
st.write("Aplikasi input nilai otomatis berbasis web.")

nama_file = "data_raport_web.xlsx"

# Membuat daftar Juz dari Juz 1 sampai Juz 30 secara otomatis
daftar_juz = [f"Juz {i}" for i in range(1, 31)]

# Membuat Form Input di Web
with st.form(key='form_raport', clear_on_submit=True):
    nama = st.text_input("Nama Santri:", placeholder="Ketik nama di sini...")
    
    # DROPDOWN OTOMATIS JUZ 1 - 30
    juz_pilihan = st.selectbox("Pilih Juz yang Dihafal:", options=daftar_juz)
    
    jumlah_surat = st.number_input("Total Jumlah Surat yang Dihafal:", min_value=0, step=1, value=0)
    
    # Tombol submit
    submit_button = st.form_submit_button(label='SIMPAN NILAI')

if submit_button:
    if nama == "":
        st.error("Nama santri gak boleh kosong, bro!")
    else:
        # Logika menentukan predikat
        if jumlah_surat >= 10:
            predikat = "Istimewa (A)"
            catatan = "Alhamdulillah, pertahankan hafalanmu!"
        elif jumlah_surat >= 5:
            predikat = "Baik (B)"
            catatan = "Bagus, tingkatkan lagi murajaahnya."
        else:
            predikat = "Kurang (D)"
            catatan = "Harus lebih giat dan sering setoran ya!"
            
        # Proses Simpan ke Excel
        data_baru = {
            "Nama Santri": [nama],
            "Juz Dihafal": [juz_pilihan],
            "Total Surat": [jumlah_surat],
            "Predikat": [predikat],
            "Catatan": [catatan]
        }
        df_baru = pd.DataFrame(data_baru)
        
        if os.path.exists(nama_file):
            df_lama = pd.read_excel(nama_file)
            df_total = pd.concat([df_lama, df_baru], ignore_index=True)
            df_total.to_excel(nama_file, index=False)
        else:
            df_baru.to_excel(nama_file, index=False)
            
        # Tampilkan Notifikasi Sukses
        st.success(f"Data {nama} berhasil disimpan!")
        st.balloons() 
        
        # Tampilkan Preview
        st.markdown(f"**Hafalan:** {juz_pilihan}")
        st.markdown(f"**Predikat:** {predikat}")
        st.markdown(f"*Catatan: {catatan}*")

# --- TOMBOL DOWNLOAD UNTUK HP/USER ---
st.write("---")
st.subheader("📂 Download Data")

if os.path.exists(nama_file):
    with open(nama_file, "rb") as file:
        st.download_button(
            label="📥 DOWNLOAD FILE EXCEL KE HP",
            data=file,
            file_name="rekap_raport_rqik.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.info("Belum ada data yang disimpan untuk di-download, bro.")
