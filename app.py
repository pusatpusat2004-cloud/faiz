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
    "11. Hud (123 Ayat)", "12. Yusuf (111 Ayat)", "13. Ar-Ra'd (43 Ayat)", "14. Ibrahim (52 Ayat)", "15. Al-Hijr (99 Ayat)",
    "16. An-Nahl (128 Ayat)", "17. Al-Isra' (111 Ayat)", "18. Al-Kahf (110 Ayat)", "19. Maryam (98 Ayat)", "20. Taha (135 Ayat)",
    "21. Al-Anbiya' (112 Ayat)", "22. Al-Hajj (78 Ayat)", "23. Al-Mu'minun (118 Ayat)", "24. An-Nur (64 Ayat)", "25. Al-Furqan (77 Ayat)",
    "26. Asy-Syu'ara' (227 Ayat)", "27. An-Naml (93 Ayat)", "28. Al-Qasas (88 Ayat)", "29. Al-'Ankabut (69 Ayat)", "30. Ar-Rum (60 Ayat)",
    "31. Luqman (34 Ayat)", "32. As-Sajdah (30 Ayat)", "33. Al-Ahzab (73 Ayat)", "34. Saba' (54 Ayat)", "35. Fatir (45 Ayat)",
    "36. Yasin (83 Ayat)", "37. As-Saffat (182 Ayat)", "38. Sad (88 Ayat)", "39. Az-Zumar (75 Ayat)", "40. Ghafir (85 Ayat)",
    "41. Fussilat (54 Ayat)", "42. Asy-Syura (53 Ayat)", "43. Az-Zukhruf (89 Ayat)", "44. Ad-Dukhan (59 Ayat)", "45. Al-Jasiyah (37 Ayat)",
    "46. Al-Ahqaf (35 Ayat)", "47. Muhammad (38 Ayat)", "48. Al-Fath (29 Ayat)", "49. Al-Hujurat (18 Ayat)", "50. Qaf (45 Ayat)",
    "51. Az-Zariyat (60 Ayat)", "52. At-Tur (49 Ayat)", "53. An-Najm (62 Ayat)", "54. Al-Qamar (55 Ayat)", "55. Ar-Rahman (78 Ayat)",
    "56. Al-Waqi'ah (96 Ayat)", "57. Al-Hadid (29 Ayat)", "58. Al-Mujadilah (22 Ayat)", "59. Al-Hasyr (24 Ayat)", "60. Al-Mumtahanah (13 Ayat)",
    "61. As-Saff (14 Ayat)", "62. Al-Jumu'ah (11 Ayat)", "63. Al-Munafiqun (11 Ayat)", "64. At-Taghabun (18 Ayat)", "65. At-Talaq (12 Ayat)",
    "66. At-Tahrim (12 Ayat)", "67. Al-Mulk (30 Ayat)", "68. Al-Qalam (52 Ayat)", "69. Al-Haqqah (52 Ayat)", "70. Al-Ma'arij (44 Ayat)",
    "71. Nuh (28 Ayat)", "72. Al-Jinn (28 Ayat)", "73. Al-Muzzammil (20 Ayat)", "74. Al-Muddassir (56 Ayat)", "75. Al-Qiyamah (40 Ayat)",
    "76. Al-Insan (31 Ayat)", "77. Al-Mursalat (50 Ayat)", "78. An-Naba' (40 Ayat)", "79. An-Nazi'at (46 Ayat)", "80. 'Abasa (42 Ayat)",
    "81. At-Takwir (29 Ayat)", "82. Al-Infitar (19 Ayat)", "83. Al-Mutaffifin (36 Ayat)", "84. Al-Insyiqaq (25 Ayat)", "85. Al-Buruj (22 Ayat)",
    "86. At-Tariq (17 Ayat)", "87. Al-A'la (19 Ayat)", "88. Al-Ghasyiyah (26 Ayat)", "89. Al-Fajr (30 Ayat)", "90. Al-Balad (20 Ayat)",
    "91. Asy-Syams (15 Ayat)", "92. Al-Lail (21 Ayat)", "93. Ad-Duha (11 Ayat)", "94. Asy-Syarh (8 Ayat)", "95. At-Tin (8 Ayat)",
    "96. Al-'Alaq (19 Ayat)", "97. Al-Qadr (5 Ayat)", "98. Al-Bayyinah (8 Ayat)", "99. Al-Zalzalah (8 Ayat)", "100. Al-'Adiyat (11 Ayat)",
    "101. Al-Qari'ah (11 Ayat)", "102. At-Takasur (8 Ayat)", "103. Al-'Asr (3 Ayat)", "104. Al-Humazah (9 Ayat)", "105. Al-Fil (5 Ayat)",
    "106. Quraisy (4 Ayat)", "107. Al-Ma'un (7 Ayat)", "108. Al-Kausar (3 Ayat)", "109. Al-Kafirun (6 Ayat)", "110. An-Nasr (3 Ayat)",
    "111. Al-Masad (5 Ayat)", "112. Al-Ikhlas (4 Ayat)", "113. Al-Falaq (5 Ayat)", "114. An-Nas (6 Ayat)"
]

# Membuat daftar Juz 1 sampai Juz 30 otomatis
daftar_juz = [f"Juz {i}" for i in range(1, 31)]

# Membuat Form Input di Web
with st.form(key='form_raport', clear_on_submit=True):
    nama = st.text_input("Nama Santri:", placeholder="Ketik nama di sini...")
    juz_pilihan = st.selectbox("Pilih Juz:", options=daftar_juz)
    surah_pilihan = st.selectbox("Nama Surah:", options=daftar_surat)
    
    # PERUBAHAN INPUTAN SESUAI REQUEST: DIUBAH JADI KOLOM KETIK MANUAL
    jumlah_hafalan = st.text_input("Jumlah Hafalan / Sampe Mana:", placeholder="Contoh: Ayat 1-7, atau Sudah hafal setengah surah")
    
    submit_button = st.form_submit_button(label='SIMPAN NILAI')

if submit_button:
    if nama == "":
        st.error("Nama santri gak boleh kosong, bro!")
    elif jumlah_hafalan == "":
        st.error("Kolom Jumlah Hafalan gak boleh kosong, bro!")
    else:
        # Pesan motivasi default yang otomatis muncul di file Excel
        catatan_selesai = "Alhamdulillah, semangat terus ya hafalan nya!"
            
        # Proses Simpan ke Excel MDTA
        data_baru = {
            "Nama Santri": [nama],
            "Pilih Juz": [juz_pilihan],
            "Nama Surah": [surah_pilihan],
            "Jumlah Hafalan / Sampe Mana": [jumlah_hafalan],
            "Setoran Hafalan Santri MDTA": [catatan_selesai]
        }
        df_baru = pd.DataFrame(data_baru)
        
        if os.path.exists(nama_file):
            df_lama = pd.read_excel(nama_file)
            df_total = pd.concat([df_lama, df_baru], ignore_index=True)
            df_total.to_excel(nama_file, index=False)
        else:
            df_baru.to_excel(nama_file, index=False)
            
        # --- EFEK SURPRISE BALON TERBANG ---
        st.success(f"Data {nama} berhasil disimpan!")
        st.balloons()
        
        # Tampilkan Preview Hasil di Layar Web
        st.markdown(f"**Nama Santri:** {nama}")
        st.markdown(f"**Juz:** {juz_pilihan} | **Surah:** {surah_pilihan}")
        st.markdown(f"**Hafalan / Sampe Mana:** {jumlah_hafalan}")
        st.markdown(f"**Setoran Hafalan Santri MDTA:** *\"{catatan_selesai}\"*")

# --- TOMBOL DOWNLOAD DATA EXCEL ---
st.write("---")
st.subheader("📂 Download Data")

if os.path.exists(nama_file):
    with open(nama_file, "rb") as file:
        st.download_button(
            label="📥 DOWNLOAD FILE EXCEL KE HP",
            data=file,
            file_name="rekap_raport_mdta.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.info("Belum ada data yang disimpan untuk di-download, bro.")
