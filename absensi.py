from datetime import datetime
import pytz

# Atur zona waktu ke Waktu Indonesia Barat (WIB)
timezone = pytz.timezone('Asia/Jakarta')
waktu_sekarang = datetime.now(timezone)

# Format tanggal dan waktu
tanggal = waktu_sekarang.strftime("%Y-%m-%d")
jam = waktu_sekarang.strftime("%H:%M:%S")

# Teks yang akan dimasukkan ke dalam file log
log_kehadiran = f"| {tanggal} | {jam} | Hadir (Otomatis via GitHub Actions) |\n"

# Tulis ke file absensi.md
try:
    with open("absensi.md", "a") as file:
        file.write(log_kehadiran)
    print(# "Absensi berhasil dicatat untuk tanggal:", tanggal)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
