
# 🎬 Movie Recommendation App (Streamlit)

Aplikasi ini merekomendasikan film berdasarkan judul film yang dipilih oleh pengguna, menggunakan pendekatan **content-based filtering**. Dengan memanfaatkan teknik seperti cosine similarity, aplikasi ini memberikan rekomendasi film yang serupa berdasarkan genre, sinopsis, atau fitur lainnya.

---

## 🚀 Fitur Utama

- **🔍 Rekomendasi film berdasarkan film yang dipilih**
- **🖼️ Tampilkan poster film dan informasi singkat**
- **⚡ Cepat dan ringan berkat Streamlit**
- **📊 Menggunakan teknik cosine similarity atau content vectorization**
- **📚 Dataset dari TMDb atau Kaggle**

---

## 🛠 Teknologi yang Digunakan

| Teknologi     | Kegunaan |
|---------------|----------|
| Python        | Bahasa pemrograman utama |
| Streamlit     | Untuk antarmuka web interaktif |
| Pandas / NumPy | Pengolahan dan analisis data |
| Scikit-learn  | Model rekomendasi dengan cosine similarity |
| Requests      | Mengambil poster film dari TMDb API |
| Pickle (`.pkl`)| Menyimpan model similarity matrix |

---

## 📦 Instalasi

1. **Clone repositori:**

```bash
git clone https://github.com/Reswn/Movie-Recommended-System.git

```

2. **Install dependensi:**

```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi:**

```bash
streamlit run app.py
```

4. **Buka di browser:**

```
http://localhost:8501
```

---

## 📂 Struktur Proyek

```
movie-recommender-streamlit/
├── app.py                # File utama aplikasi Streamlit
├── model.pkl             # Model similarity matrix (pickle)
├── movies.csv            # Dataset film
├── requirements.txt      # Daftar dependensi
└── README.md             # Dokumentasi ini
```

---

## 🧠 Cara Kerja Aplikasi

1. Dataset film dibaca dari file `movies.csv`.
2. Judul film yang dipilih oleh pengguna digunakan untuk mencari vektor fiturnya.
3. Kemiripan dihitung menggunakan **cosine similarity**.
4. Rekomendasi film serupa ditampilkan bersama dengan poster dan informasi singkat.

---

## 🔑 Konfigurasi API Key (Opsional)

Jika menggunakan **TMDb API** untuk menampilkan poster film:

1. Buat file `.env` di root direktori:

```env
TMDB_API_KEY=your_tmdb_key_here
```

2. Di dalam kode, tambahkan:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
```

3. Install library tambahan jika belum:

```bash
pip install python-dotenv requests
```

---

## 📋 Contoh Penggunaan

**Input:**
- Film yang dipilih: *Avatar*

**Output:**
> Rekomendasi film:
> - Titanic
> - Guardians of the Galaxy
> - Avengers
> - Inception  
> *(Disertai poster & deskripsi singkat masing-masing film)*

---

## 📈 Perkembangan Selanjutnya (Ide Fitur Tambahan)

- Rekomendasi berdasarkan rating pengguna (**collaborative filtering**)
- Tambahkan fitur login pengguna
- Simpan histori rekomendasi
- Filter film berdasarkan kategori (genre, populer, terbaru)
- Menampilkan trailer film

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan fork repositori ini, lakukan perubahan, dan kirimkan **Pull Request (PR)**. Berikut beberapa ide kontribusi:
- Menambahkan model rekomendasi baru
- Mendukung bahasa Indonesia
- Meningkatkan UI/UX aplikasi

---

## 📬 Kontak

- **📧 Email:** renisuwandi1011@gmail.com  
- **🌐 GitHub:** [@Reswn](https://github.com/Reswn)

---

## 📄 Lisensi

Proyek ini tersedia di bawah lisensi MIT. Silakan lihat file [`LICENSE`](LICENSE) untuk detail lebih lanjut.

---

## 🙏 Terima Kasih!

Terima kasih telah menggunakan Movie Recommendation App ini. Jika ada pertanyaan, masukan, atau ingin berkontribusi, jangan ragu untuk hubungi saya via email atau GitHub. Semoga proyek ini bermanfaat bagi Anda! 🚀

---
