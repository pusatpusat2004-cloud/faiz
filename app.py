import streamlit as st
import pandas as pd
import os

# Set judul halaman web
st.set_page_config(page_title="Nilai Hafalan", page_icon="📝", layout="centered")

st.title("📝 Nilai Hafalan Santriwan dan santriwati MDTA ")
st.write("Aplikasi input nilai otomatis berbasis web.")

nama_file = "data_raport_web.xlsx"

# Daftar 114 Nama Surat Al-Qur'an otomatis
daftar_surat = [
    "1. Al-Fatihah", "2. Al-Baqarah", "3. Ali 'Imran", "4. An-Nisa'", "5. Al-Ma'idah",
    "6. Al-An'am", "7. Al-A'raf", "8. Al-Anfal", "9. At-Taubah", "10. Yunus",
    "11. Hud", "12. Yusuf", "13. Ar-Ra'd", "14. Ibrahim", "15. Al-Hijr",
    "16. An-Nahl", "17. Al-Isra'", "18. Al-Kahf", "19. Maryam", "20. Taha",
    "21. Al-Anbiya'", "22. Al-Hajj", "23. Al-Mu'minun", "24. An-Nur", "25. Al-Furqan",
    "26. Asy-Syu'ara'", "27. An-Naml", "28. Al-Qasas", "29. Al-'Ankabut", "30. Ar-Rum",
    "31. Luqman", "32. As-Sajdah", "33. Al-Ahzab", "34. Saba'", "35. Fatir",
    "36. Yasin", "37. As-Saffat", "38. Sad", "39. Az-Zumar", "40. Ghafir",
    "41. Fussilat", "42. Asy-Syura", "43. Az-Zukhruf", "44. Ad-Dukhan", "45. Al-Jasiyah",
    "46. Al-Ahqaf", "47. Muhammad", "48. Al-Fath", "49. Al-Hujurat", "50. Qaf",
    "51. Az-Zariyat", "52. At-Tur", "53. An-Najm", "54. Al-Qamar", "55. Ar-Rahman",
    "56. Al-Waqi'ah", "57. Al-Hadid", "58. Al-Mujadilah", "59. Al-Hasyr", "60. Al-Mumtahanah",
    "61. As-Saff", "62. Al-Jumu'ah", "63. Al-Munafiqun", "64. At-Taghabun", "65. At-Talaq",
    "66. At-Tahrim", "67. Al-Mulk", "68. Al-Qalam", "69. Al-Haqqah", "70. Al-Ma'arij",
    "71. Nuh", "72. Al-Jinn", "73. Al-Muzzammil", "74. Al-Muddassir", "75. Al-Qiyamah",
    "76. Al-Insan", "77. Al-Mursalat", "78. An-Naba'", "79. An-Nazi'at", "80. 'Abasa",
    "81. At-Takwir", "82. Al-Infitar", "83. Al-Mutaffifin", "84. Al-Insyiqaq", "85. Al-Buruj",
    "86. At-Tariq", "87. Al-A'la", "88. Al-Ghasyiyah", "89. Al-Fajr", "90. Al-Balad",
    "91. Asy-Syams", "92. Al-Lail", "93. Ad-Duha", "94. Asy-Syarh", "95. At-Tin",
    "96. Al-'Alaq", "97. Al-Qadr", "98. Al-Bayyinah", "99. Al-Zalzalah", "100. Al-'Adiyat",
    "101. Al-Qari'ah", "102. At-Takasur", "103. Al-'Asr", "104. Al-Humazah", "105. Al-Fil",
    "106. Quraisy", "107. Al-Ma'un", "108. Al-Kausar", "109. Al-Kafirun", "110. An-Nasr",
    "111. Al-Masad", "112. Al-Ikhlas", "113. Al-Falaq", "114. An-Nas"
]

# Membuat daftar Juz 1 sampai Juz 30 otomatis
daftar_juz = [f"Juz {i}" for i in range(1, 31)]

# Membuat Form Input di Web Berdasarkan Request Baru
with st.form(key='form_raport', clear_on_submit=True):
    nama = st.text_input("Nama Santri:", placeholder="Ketik nama di sini...")
    
    # DROPDOWN PILIH JUZ
    juz_pilihan = st.selectbox("Pilih Juz:", options=daftar_juz)
    
    # DROPDOWN NAMA SURAH OTOMATIS (Tinggal Scroll & Klik)
    surah_pilihan = st.selectbox("Nama Surah:", options=daftar_surat)
    
    # INPUTAN AYAT
    ayat = st.text_input("Ayat:", placeholder="")
    
    # Tombol submit
    submit_button = st.form_submit_button(label='SIMPAN NILAI')

if submit_button:
    if nama == "":
        st.error("Nama santri gak boleh kosong, bro!")
    elif ayat == "":
        st.error("Kolom Ayat harus diisi, bro!")
    else:
        # Proses Simpan ke Excel dengan Format Kolom Baru
        data_baru = {
            "Nama Santri": [nama],
            "Pilih Juz": [juz_pilihan],
            "Nama Surah": [surah_pilihan],
            "Ayat": [ayat]
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
        
        # Tampilkan Preview Hasil Inputan Baru
        st.markdown(f"**Nama Santri:** {nama}")
        st.markdown(f"**Juz:** {juz_pilihan}")
        st.markdown(f"**Surah:** {surah_pilihan}")
        st.markdown(f"**Ayat:** {ayat}")

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
    st.info("Belum ada data yang disimpan untuk di-download.")
