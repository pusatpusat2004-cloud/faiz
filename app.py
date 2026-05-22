import streamlit as st
import pandas as pd
import os

# Set judul halaman web (muncul di tab browser & pratinjau WA)
st.set_page_config(page_title="Hafalan Santri MDTA", page_icon="📝", layout="centered")

# --- MENAMPILKAN LOGO MAJELIS ---
if os.path.exists("logo_majelis.png"):
    st.image("logo_majelis.png", width=100)

# --- JUDUL UTAMA ---
st.title("Nilai Hafalan Santri MDTA")
st.write("Aplikasi input nilai otomatis berbasis web.")

nama_file = "data_raport_mdta.xlsx"

# Daftar 114 Nama Surat Al-Qur'an lengkap dengan jumlah ayatnya
daftar_surat = [
    "1. Al-Fatihah (7 Ayat)", "2. Al-Baqarah (286 Ayat)", "3. Ali 'Imran (200 Ayat)", "4. An-Nisa' (176 Ayat)", "5. Al-Ma'idah (120 Ayat)",
    "6. Al-An'am (165 Ayat)", "7. Al-A'raf (206 Ayat)", "8. Al-Anfal (75 Ayat)", "9. At-Taubah (129 Ayat)", "10. Yunus (109 Ayat)",
    "11. Hud (123 Ayat)", "1
