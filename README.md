# Laporan Proyek Machine Learning - RENI KARTIKA SUWANDI
![Cover](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/Sampul.jpg?raw=true) 

## Project Overview
Anime merupakan salah satu bentuk hiburan visual yang sangat populer, terutama di kalangan generasi muda. Kepopulerannya tidak hanya terbatas di Jepang, tetapi juga telah merambah hingga ke berbagai belahan dunia, termasuk Indonesia. Namun, tingginya minat terhadap anime juga membawa tantangan tersendiri, yakni banyaknya jumlah judul dan ragam genre yang membuat pengguna kesulitan memilih tontonan yang sesuai dengan selera mereka. Oleh karena itu, sistem rekomendasi menjadi solusi penting untuk mempermudah pengguna dalam menemukan anime yang relevan dan menarik bagi mereka. Sistem seperti ini bertujuan untuk menyederhanakan proses pencarian dan meningkatkan kepuasan pengguna terhadap platform penyedia layanan tontonan.

Dalam studi oleh Sitanggang et al. (2023), dijelaskan bahwa sistem rekomendasi anime sangat membantu pengguna untuk menemukan judul yang sesuai dengan preferensi mereka dengan cara memprediksi item yang relevan melalui pendekatan berbasis data seperti Singular Value Decomposition (SVD) dan Cosine Similarity [1]. Hal ini membuktikan bahwa metode sistem rekomendasi telah terbukti mampu meningkatkan pengalaman pengguna secara signifikan. Berdasarkan pemahaman tersebut, proyek ini berfokus pada pembuatan sistem rekomendasi anime yang menggabungkan pendekatan content-based filtering serta algoritma supervised learning seperti K-Nearest Neighbor, Random Forest, dan Gradient Boosting. Sistem ini diharapkan mampu menyajikan rekomendasi anime yang lebih akurat dan personal sesuai dengan karakteristik pengguna.

Referensi:

[1] A. Sitanggang, A. D. Harahap, A. Karimullah, Y. A. Dewantara, C. Rozikin, “Sistem Rekomendasi Anime Menggunakan Metode Singular Value Decomposition (SVD) dan Cosine Similarity,” Ilmu Komputer, Universitas Singaperbangsa Karawang, 2023.


## Business Understanding
Di tengah pertumbuhan pesat industri hiburan digital, khususnya anime, platform penyedia layanan tontonan menghadapi tantangan besar dalam mempertahankan pengalaman pengguna yang personal dan memuaskan. Ribuan judul anime dengan berbagai genre dirilis setiap tahunnya, menyebabkan pengguna kesulitan untuk menemukan tontonan yang benar-benar sesuai dengan preferensi mereka. Ketidaktepatan dalam memberikan rekomendasi tidak hanya menurunkan kepuasan pengguna, tetapi juga berpotensi menurunkan loyalitas dan retensi pengguna terhadap platform tersebut.

Situasi ini menciptakan urgensi tinggi bagi platform untuk mengembangkan sistem rekomendasi yang lebih cerdas dan kontekstual. Sistem seperti ini tidak hanya menyederhanakan proses pencarian konten, tetapi juga secara langsung mendukung strategi bisnis utama, yaitu mempertahankan pengguna, meningkatkan engagement, dan memaksimalkan waktu tayang per pengguna. Pengembangan sistem rekomendasi yang akurat dan adaptif telah menjadi kebutuhan strategis, bukan lagi fitur tambahan.

### Problem Statements

- Pengguna kesulitan menemukan anime yang sesuai dengan preferensi mereka karena banyaknya pilihan judul dan genre.
- Sistem rekomendasi pada beberapa platform belum mampu memberikan saran yang akurat dan relevan terhadap minat pengguna.
- Kurangnya pemanfaatan algoritma pembelajaran mesin (machine learning) yang lebih canggih dalam sistem rekomendasi.

### Goals
- Membangun sistem rekomendasi yang dapat memberikan saran anime yang relevan berdasarkan data preferensi pengguna.
- Meningkatkan akurasi dan personalisasi rekomendasi dengan menerapkan algoritma terbaik diantara Random Forest, KNN, dan Gradient Boosting.
- Mengintegrasikan pendekatan content-based filtering untuk menghasilkan rekomendasi yang lebih kontekstual dan adaptif terhadap profil pengguna.


### **Solution Approach**
Untuk mencapai tujuan proyek dalam memberikan rekomendasi anime yang sesuai dengan preferensi pengguna, berikut beberapa pendekatan teknis dan algoritmik yang diterapkan:

### 1. Eksplorasi dan Pra-pemrosesan Data

Langkah awal dilakukan eksplorasi data (*Exploratory Data Analysis / EDA*) untuk memahami struktur dataset serta mengidentifikasi pola dan anomali seperti nilai kosong (`NaN`) atau tidak valid pada kolom *Popularity* dan *Rank*. 

Setelah itu, proses pembersihan data dilakukan dengan:

- Menghapus entri yang tidak valid.
- Melakukan normalisasi skor dan encoding fitur kategorikal seperti genre menggunakan `MultiLabelBinarizer`.
- Mengubah deskripsi teks anime menjadi representasi numerik melalui `TF-IDF Vectorizer`, agar dapat digunakan dalam pencarian berbasis konten.

### 2. Sistem Rekomendasi Berbasis Konten (Content-Based Filtering)

Representasi vektor dari fitur konten seperti deskripsi dan genre digunakan untuk menghitung kemiripan antar-anime menggunakan metrik *cosine similarity*. Dengan pendekatan ini, sistem dapat memberikan rekomendasi berdasarkan kedekatan konten dengan anime yang sedang ditinjau atau disukai oleh pengguna.

### 3. Eksperimen Penggabungan Fitur

Untuk meningkatkan akurasi rekomendasi, berbagai jenis fitur — seperti vektor TF-IDF deskripsi, encoding genre, dan skor popularitas/rating — digabungkan Kombinasi fitur ini untuk memberikan representasi yang lebih kaya dan informatif, sehingga perhitungan kemiripan menjadi lebih presisi.

### 4. Model Prediksi dan Sistem Top-N Recommendation

Untuk menghasilkan daftar Top-N anime yang relevan bagi pengguna, beberapa model pembelajaran mesin diuji coba dalam memprediksi skor preferensi pengguna terhadap suatu anime, beberapa algoritma machine learning diuji coba untuk memprediksi skor preferensi pengguna terhadap anime, termasuk KNN, Random Forest, dan Gradient Boosting. Hasil prediksi digunakan bersama cosine similarity untuk menampilkan daftar Top-N anime yang paling relevan bagi pengguna.


### 5. Evaluasi dan Pemilihan Model Terbaik

Evaluasi model dilakukan melalui dua pendekatan utama:
- **Evaluasi kuantitatif**: Menggunakan metrik RMSE dan R² untuk membandingkan akurasi prediksi model.

---

## **Data Understanding**
### **1. Informasi Dataset**
Metadata Dataset

| **Jenis Informasi**        | **Keterangan**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| **Title**                  | Anime Dataset 2023                                                             |
| **Source**                 | [Kaggle](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset)        |
| **Maintainer**             | Sajid                                                                            |
| **License**                | Database: Open Database, Contents: Database Contents                            |
| **Visibility**             | Publik                                                                           |
| **Tags**                   | Arts and Entertainment, Movies and TV Shows, Anime and Manga, Popular Culture, Japan |
| **Usability Score**        | 10.00 / 10                                                                       |

### **2. Struktur Data**
Dataset terdiri dari informasi lengkap mengenai berbagai judul anime, termasuk detail genre, deskripsi, skor rating, popularitas, dan metadata lainnya. Dengan data ini, sistem rekomendasi dapat dibangun menggunakan pendekatan *content-based filtering* untuk memberikan saran anime sesuai preferensi pengguna.

---
### **3. Exploratory Data Analysis**
### 3.1 Informasi 5 Baris Pertama Dataset

Berikut merupakan tampilan lima baris pertama dari dataset anime yang digunakan dalam proyek ini:

| anime_id | Name                                 | English name                 | Other name                                    | Score | Genres                                       | Synopsis                                                                 | Type  | Episodes | Aired                            | Studios        | Source   | Duration          | Rating                       | Rank   | Popularity | Favorites | Scored By | Members  | Image URL                                      |
|----------|--------------------------------------|------------------------------|---------------------------------------------|-------|--------------------------------------------|--------------------------------------------------------------------------|-------|----------|----------------------------------|----------------|----------|-------------------|------------------------------|--------|------------|-----------|-----------|----------|------------------------------------------------|
| 1        | Cowboy Bebop                         | Cowboy Bebop                 | カウボーイビバップ                           | 8.75  | Action, Award Winning, Sci-Fi              | Crime is timeless...                                                   | TV    | 26         | Apr 3, 1998 to Apr 24, 1999     | Sunrise        | Original | 24 min per ep     | R - 17+                        | 41.0   | 43         | 78525     | 914193.0  | 1771505  | https://cdn.myanimelist.net/images/anime/4/196...  |
| 5        | Cowboy Bebop: Tengoku no Tobira      | Cowboy Bebop: The Movie      | カウボーイビバップ 天国の扉                  | 8.38  | Action, Sci-Fi                             | Another day, another bounty...                                         | Movie | 1          | Sep 1, 2001                     | Bones          | Original | 1 hr 55 min       | R - 17+                        | 189.0  | 602        | 1448      | 206248.0  | 360978   | https://cdn.myanimelist.net/images/anime/1439/... |
| 6        | Trigun                               | Trigun                       | トライガン                                   | 8.22  | Action, Adventure, Sci-Fi                  | Vash the Stampede is the man with a $60,000,000 bounty...              | TV    | 26         | Apr 1, 1998 to Sep 30, 1998     | Madhouse       | Manga    | 24 min per ep     | PG-13                          | 328.0  | 246        | 15035     | 356739.0  | 727252   | https://cdn.myanimelist.net/images/anime/7/203...  |
| 7        | Witch Hunter Robin                   | Witch Hunter Robin           | Witch Hunter ROBIN (ウイッチハンターロビン) | 7.25  | Action, Drama, Mystery, Supernatural       | Robin Sena is a powerful craft user drafted into an agency...          | TV    | 26         | Jul 3, 2002 to Dec 25, 2002     | Sunrise        | Original | 25 min per ep     | PG-13                          | 2764.0 | 1795       | 613       | 42829.0   | 111931   | https://cdn.myanimelist.net/images/anime/10/19...  |
| 8        | Bouken Ou Beet                       | Beet the Vandel Buster       | 冒険王ビィト                                 | 6.94  | Adventure, Fantasy, Supernatural           | It is the dark century and the people are suffering under darkness...  | TV    | 52         | Sep 30, 2004 to Sep 29, 2005    | Toei Animation | Manga    | 23 min per ep     | PG - Children                    | 4240.0 | 5126       | 14        | 6413.0    | 15001    | https://cdn.myanimelist.net/images/anime/7/215...  |


> **Catatan**: Setiap baris merepresentasikan informasi tentang satu judul anime, mulai dari nama, genre, deskripsi, hingga metadata seperti studio dan durasi.



### 3.2 Variabel Dataset Anime Recommendation

Dataset ini berisi informasi lengkap mengenai berbagai judul anime, termasuk deskripsi, genre, popularitas, rating, dan metadata lainnya yang relevan untuk membangun sistem rekomendasi berbasis konten (*content-based filtering*). Berikut adalah deskripsi masing-masing variabel:

| Nama Variabel         | Deskripsi                                                                                             |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| `anime_id`            | ID unik untuk setiap judul anime.                                                                     |
| `Name`                | Judul utama dari anime dalam bahasa Jepang atau bahasa asli.                                          |
| `English name`        | Judul alternatif dalam bahasa Inggris (jika tersedia).                                                |
| `Other name`          | Judul lain dari anime, seperti versi terjemahan atau nama lokal di negara lain.                      |
| `Score`               | Skor rata-rata yang diberikan oleh pengguna MyAnimeList (skala 1–10).                                 |
| `Genres`              | Genre dari anime, seperti Action, Adventure, Romance, dll. Bisa lebih dari satu genre per judul.     |
| `Synopsis`            | Ringkasan cerita dari anime, digunakan sebagai fitur teks untuk sistem pencarian berbasis konten.    |
| `Type`                | Jenis konten anime, misalnya TV, Movie, OVA, Special, dsb.                                           |
| `Episodes`            | Jumlah episode atau durasi total dari anime (untuk Movie biasanya hanya 1).                           |
| `Aired`               | Periode kapan anime ditayangkan, mulai dari tanggal awal hingga akhir siaran.                         |
| `Premiered`           | Musim anime tersebut pertama kali tayang, seperti "Spring 2023", "Fall 2022", dsb.                    |
| `Status`              | Status penyelesaian anime: Finished Airing, Currently Airing, atau Not Yet Aired.                    |
| `Producers`           | Studio atau perusahaan yang memproduksi anime.                                                       |
| `Licensors`           | Pihak yang memiliki hak distribusi resmi atas anime tersebut.                                        |
| `Studios`             | Studio animasi yang bertanggung jawab atas produksi anime.                                           |
| `Source`              | Sumber asal cerita anime, seperti Manga, Light Novel, Game, dsb.                                     |
| `Duration`            | Durasi rata-rata tiap episode atau total durasi untuk Movie.                                         |
| `Rating`              | Klasifikasi usia penonton, seperti "R - 17+", "PG-13", atau "G - All Ages".                           |
| `Rank`                | Peringkat anime berdasarkan skor dan popularitas relatif terhadap anime lainnya.                     |
| `Popularity`          | Indeks popularitas anime; semakin rendah angka, semakin populer anime tersebut.                      |
| `Favorites`           | Jumlah pengguna yang menambahkan anime ke daftar favorit mereka.                                     |
| `Scored By`           | Jumlah pengguna yang memberikan rating pada anime tersebut.                                          |
| `Members`             | Jumlah pengguna yang memiliki anime ini di daftar mereka.                                            |
| `Image URL`           | Tautan gambar sampul/resmi anime dari sumber MyAnimeList.                                            |

> Catatan: Seluruh data bersifat informatif dan dapat digunakan untuk membangun model rekomendasi yang personal sesuai preferensi pengguna.

---

### 3.3 Ringkasan Informasi Dataset

Dataset yang digunakan dalam proyek sistem rekomendasi anime ini memiliki struktur sebagai berikut:

#### **Ukuran Dataset:**
- **Jumlah Baris**: 24.905 entri anime
- **Jumlah Kolom**: 24 kolom (variabel)

#### **Tipe Data:**
- **Fitur Numerik (`int64`) → 4 kolom**:
  - `anime_id`, `Popularity`, `Favorites`, `Members`
- **Fitur Teksual/Kategorikal (`object`) → 20 kolom**:
  - `Name`, `English name`, `Other name`, `Score`, `Genres`, `Synopsis`, `Type`, `Episodes`, `Aired`, `Premiered`, `Status`, `Producers`, `Licensors`, `Studios`, `Source`, `Duration`, `Rating`, `Rank`, `Scored By`, `Image URL`

#### **Target Variabel:**
Tidak ada target eksplisit seperti dalam kasus regresi atau klasifikasi, karena ini adalah proyek sistem rekomendasi. Namun, beberapa fitur penting yang digunakan untuk rekomendasi antara lain:
- `Genres`: Digunakan untuk encoding dan representasi vektor genre.
- `Synopsis`: Diubah menjadi vektor numerik dengan TF-IDF untuk pencarian berbasis konten.
- `Score`, `Rank`, `Popularity`: Digunakan sebagai indikator kualitas dan popularitas anime.

#### **Ciri Statistik dan Distribusi Data:**
- Semua kolom **tidak memiliki missing values**, sehingga tidak memerlukan imputasi.
- Beberapa kolom numerik seperti `Score`, `Episodes`, `Rank`, dan `Scored By` saat ini masih bertipe `object` dan perlu dikonversi ke tipe numerik sebelum analisis lanjutan.
- Dataset mencakup variasi besar jenis anime, dari anime populer dengan skor tinggi hingga yang kurang dikenal.
- Terdapat potensi outlier pada kolom `Favorites` dan `Members` karena perbedaan jumlah yang signifikan antar-anime.
- Fitur teks seperti `Synopsis` dan `Genres` membutuhkan proses preprocessing seperti tokenisasi, stopword removal, dan vectorization agar dapat digunakan dalam model rekomendasi.

### 4. Analisis Visualisasi

#### 4.1 Top 15 Anime Genres

Salah satu aspek penting dalam analisis dataset anime adalah memahami distribusi genre yang paling umum di antara judul-judul anime. Berikut adalah visualisasi frekuensi genre anime teratas berdasarkan dataset:

![Top 15 Anime Genres](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/Top%2015%20Anime%20Genre.png)

#### Insight Utama:
- **Genre Terpopuler**: Genre `Comedy` memiliki frekuensi tertinggi dengan lebih dari 7.000 entri, menjadikannya genre anime paling banyak digunakan dalam dataset.
- **Kedua dan Ketiga**: Genre `Fantasy` dan `UNKNOWN` mengikuti genre `Comedy` dengan frekuensi masing-masing sekitar 5.200 dan 4.900.
- **Genre Klasik**: Genre seperti `Action`, `Adventure`, dan `Sci-Fi` juga sangat populer, dengan frekuensi masing-masing sekitar 3.800–4.800.
- **Genre Minor**: Beberapa genre seperti `Sports`, `Avant Garde`, dan `Ecchi` memiliki frekuensi yang lebih rendah, menunjukkan bahwa mereka kurang umum dibandingkan genre utama.

#### 4.2 Analisis Popularitas
![Populer](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/Anime%20populer.png)
#### Insight Utama:
- **Shingeki no Kyojin** menjadi anime paling populer dengan `Popularity = 1`.
- Genre utama dari anime-anime ini umumnya adalah **Action**, **Adventure**, dan **Fantasy**, menunjukkan bahwa genre tersebut sangat diminati oleh komunitas MyAnimeList.
- Beberapa judul legendaris seperti **Naruto** dan **Death Note** masih memiliki posisi tinggi meskipun sudah lama dirilis, membuktikan daya tarik jangka panjang dari anime berkualitas tinggi.

#### 4.3 Analisis Top 10 Anime dengan Rank Tertinggi
![Top 10 Anime Rank](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/anime%20rating%20highest.png)
#### Insight Utama:
- **Fullmetal Alchemist: Brotherhood** menduduki peringkat pertama dengan skor rata-rata hampir sempurna (>9.15), menjadikannya salah satu anime paling dikagumi di komunitas.
- Serial **Gintama** muncul dalam beberapa versi, menunjukkan bahwa franchise ini tidak hanya populer tetapi juga konsisten menghasilkan kualitas cerita yang baik.
- **Hunter x Hunter (2011)** berada di peringkat 10, meskipun sering dianggap sebagai salah satu anime dengan cerita paling kompleks dan strategis.

#### 4.4 Distribusi Data Popularity vs Rank
![Plot Popularity vs Rank](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/popularity%20vs%20rank.png)

##### Insight Utama dari Scatter Plot Popularity vs. Rank

1. **Hubungan Popularity dan Rank**  
   - Anime dengan **popularitas tinggi** (angka besar) biasanya memiliki **peringkat rendah** (angka kecil), dan sebaliknya.
   - Ini menunjukkan bahwa anime populer cenderung mendapat peringkat lebih baik karena banyak pengguna yang menilainya.

2. **Distribusi Data**
   - Sebagian besar anime berada di area **kiri bawah grafik**, artinya mereka memiliki **popularitas rendah hingga sedang** dan **peringkat moderat hingga tinggi**.
   - Hanya sedikit anime yang sangat **populer dan berperingkat tinggi**, sehingga area **kanan atas** tampak jarang.

3. **Outlier**
   - Beberapa anime **tidak mengikuti pola umum**, misalnya:
     - Populer rendah tapi peringkat tinggi → anime berkualitas tetapi belum terlalu dikenal.
     - Populer tinggi tapi peringkat rendah → anime populer tetapi mungkin kontroversial atau tidak dinilai maksimal oleh penggemar.

---

### 5. Interpretasi untuk Sistem Rekomendasi
- Menggunakan **popularitas** sebagai faktor awal rekomendasi untuk pengguna baru, karena anime populer cenderung aman dan diminati banyak orang.
- Menggabungkan dengan **peringkat** untuk memastikan kualitas anime tetap terjaga dan sesuai preferensi pengguna.
- Anime dengan **peringkat tinggi tapi popularitas rendah** bisa direkomendasikan untuk pengguna yang ingin menjelajahi judul unik atau niche.



---
## Data Preparation
Pada tahap ini, data dipersiapkan agar siap digunakan dalam proses pembangunan sistem rekomendasi berbasis konten (content-based filtering ). Tujuan dari data preparation adalah memastikan data bersih, konsisten, dan dalam format yang tepat sehingga dapat memberikan rekomendasi yang relevan dan akurat bagi pengguna. Berikut adalah langkah-langkah yang dilakukan:

### **1. Pembersihan Data**
### 1.1 Penanganan Missing Values & Tipe Data  
Beberapa kolom seperti `Score`, `Episodes`, dan `Scored By` masih berbentuk string (`object`) dan mengandung nilai `'Unknown'`. Untuk memastikan akurasi dan kompatibilitas dalam proses rekomendasi dan prediksi:

- Nilai `'Unknown'` diubah menjadi `NaN`, lalu dikonversi ke tipe numerik menggunakan `pd.to_numeric`.
- Baris dengan missing values pada fitur penting (`Genres`, `Score`, dan `Synopsis`) dihapus karena informasi ini merupakan dasar dari sistem rekomendasi.
- Index data direset agar urut dan mudah digunakan dalam pemrosesan selanjutnya.

#### Tujuan:
- Memastikan semua fitur penting memiliki data valid dan siap digunakan.
- Mencegah error saat modeling akibat ketidakkonsistenan tipe data atau missing values.

---

### 1.2 Format Genre dan Synopsis  
Kolom `Genres` dan `Synopsis` diproses agar representasi konten menjadi seragam dan informatif:

- `Genres` yang awalnya berupa string (misalnya `"Action, Adventure"`) dipisahkan menjadi list untuk encoding multi-label.
- `Synopsis` dibersihkan dari karakter non-alfabet dan diubah menjadi huruf kecil (*lowercase*) agar konsisten dalam analisis teks.

#### Tujuan:
- Menghindari duplikasi genre yang sama tetapi format berbeda.
- Menyeragamkan teks deskripsi agar tidak ada bias akibat kapitalisasi atau karakter aneh.
- Siap untuk vektorisasi dan encoding lebih lanjut.

---

### **2. Encoding Fitur Kategorikal**

Fitur seperti `Type` dan `Rating` bersifat kategorikal dan tidak dapat langsung digunakan oleh model machine learning. Oleh karena itu, dilakukan Label Encoding untuk mengubahnya menjadi bentuk numerik.

#### Tujuan:
- Merubah data kualitatif menjadi bentuk yang dapat diproses oleh algoritma machine learning.
- Memudahkan integrasi fitur kategorikal ke dalam matriks gabungan untuk rekomendasi.

---

### **3. Normalisasi Fitur Numerik**

Beberapa fitur numerik seperti `Score`, `Members`, dan `Popularity` dinormalisasi ke dalam skala `[0, 1]` menggunakan `MinMaxScaler`.

#### Tujuan:
- Menyamakan skala antar-fitur agar tidak ada fitur yang mendominasi secara tidak proporsional.
- Membantu model machine learning bekerja lebih stabil dan akurat, terutama untuk algoritma yang sensitif terhadap skala data seperti KNN dan Gradient Boosting.

---

### **4. Ekstraksi Informasi Tambahan**

Untuk menambah kedalaman dan personalisasi rekomendasi, dilakukan ekstraksi informasi tambahan dari kolom teks:

- **Kolom `Aired`**: Diekstrak tahun rilis anime menggunakan *regular expression*.
- **Kolom `Premiered`**: Diambil musim penayangan sebagai metadata tambahan.

#### Tujuan:
- Menambah konteks waktu dalam rekomendasi (misalnya: anime populer di tahun tertentu).
- Memberikan variasi rekomendasi berdasarkan tren waktu atau musim.

---

### **5. Vektorisasi Fitur Teksual**

Agar bisa digunakan dalam perhitungan kemiripan dan model machine learning, dua fitur teksual diubah menjadi representasi numerik:

#### a. **TF-IDF Vectorizer – untuk Synopsis**
Deskripsi anime (`Synopsis`) diubah menjadi vektor TF-IDF dengan maksimal 5000 fitur kata kunci. Teknik ini membantu sistem memahami makna cerita dan mengukur kedekatan semantik antar-anime.

#### Tujuan:
- Membuat representasi teks deskripsi yang informatif dan dapat diukur secara matematis.
- Digunakan dalam cosine similarity dan model regresi/prediksi skor.

#### b. **MultiLabelBinarizer – untuk Genres**
Genre yang berbentuk list (misalnya: `"Action, Fantasy"`) diubah menjadi vektor biner untuk menangkap kombinasi genre dalam satu judul anime.

#### Tujuan:
- Mengubah genre menjadi bentuk yang bisa diolah dalam perhitungan matematika.
- Menangkap hubungan multi-label antar-genre untuk rekomendasi yang lebih presisi.

---

### **6. Penggabungan Semua Fitur**

Seluruh fitur yang telah diproses — termasuk:
- Representasi genre (binary)
- Deskripsi (TF-IDF)
- Metadata kategorikal (Type, Rating) yang sudah di-encode
- Fitur numerik yang ternormalisasi (Score, Members, Popularity)

digabungkan menggunakan fungsi `hstack()` dari `scipy.sparse` untuk membentuk sebuah matriks fitur gabungan (*combined feature matrix*).

#### Tujuan:
- Menggabungkan semua jenis fitur (teks, kategori, numerik) dalam satu representasi vektor tunggal.
- Menjadi input utama untuk proses rekomendasi dan prediksi skor anime.

---

### **7. Pembagian Data Latih dan Uji**

Jika ingin melakukan evaluasi model secara kuantitatif (misalnya dengan RMSE dan R²), dataset dibagi menjadi dua subset:

- **80% data latih**: untuk melatih model memprediksi skor anime.
- **20% data uji**: untuk menguji akurasi model secara objektif.

Pembagian dilakukan menggunakan `train_test_split` dari `sklearn.model_selection` dengan `random_state=42` agar hasilnya reprodusibel.

#### Tujuan:
- Memvalidasi performa model secara objektif.
- Memastikan bahwa model tidak hanya hafal data latih (overfitting), tetapi juga generalisasi baik ke data baru.

---

### 8. Ringkasan Tahapan Preprocessing

| No | Langkah                      | Alasan Perlu Dilakukan                                      | Tujuan Utama                                                                 |
|----|------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------|
| 1  | Pembersihan Data             | Dataset awal mengandung nilai 'Unknown' dan tipe data tidak sesuai | Memastikan data siap untuk proses encoding, vektorisasi, dan modeling         |
| 2  | Encoding Kategorikal          | Fitur `Type` dan `Rating` tidak bisa diproses oleh model ML   | Merubah data kategorikal menjadi bentuk numerik agar bisa digunakan dalam model |
| 3  | Normalisasi Numerik           | Skala fitur berbeda-beda (misalnya Score vs Members)         | Menyamakan bobot fitur agar tidak ada dominasi dari skala                    |
| 4  | Ekstraksi Informasi Tambahan | Menambah konteks tambahan seperti tahun dan musim              | Memperkaya metadata untuk rekomendasi berbasis tren                          |
| 5  | Vektorisasi Fitur Teksual    | Anime direpresentasikan dalam bentuk vektor numerik          | Mempertimbangkan konten dan genre dalam rekomendasi                           |
| 6  | Penggabungan Fitur           | Menggabungkan semua jenis fitur dalam satu matriks           | Membentuk representasi komplit setiap anime                                  |
| 7  | Pembagian Data Latih & Uji  | Untuk pengujian model secara kuantitatif                     | Mengukur performa model secara objektif dengan metrik seperti RMSE dan R²      |

---

Modeling 
---

Pada tahap ini, dibangun sistem rekomendasi berbasis konten (*Content-Based Filtering*) dan diuji coba beberapa model regresi untuk memprediksi skor anime. Tujuan dari tahapan ini adalah menghasilkan **Top-N rekomendasi anime** yang relevan berdasarkan konten dan genre dari judul input.

### 1. Content-Based Filtering dengan Cosine Similarity

#### Deskripsi Pendekatan  
Sistem rekomendasi berbasis konten bekerja dengan cara merepresentasikan setiap anime sebagai vektor numerik berdasarkan fitur-fitur seperti `Genre`, `Synopsis`, `Type`, `Rating`, dan metadata lainnya. Setelah semua anime direpresentasikan dalam bentuk vektor, dilakukan perhitungan kemiripan menggunakan metrik *cosine similarity*.

Setiap anime direpresentasikan sebagai vektor gabungan dari:
- Genre (dengan `MultiLabelBinarizer`)
- Deskripsi (dengan `TF-IDF Vectorizer`)
- Metadata tambahan seperti `Type`, `Rating`, `Score`, `Members`, dan `Popularity` yang dinormalisasi

#### Metrik Kemiripan: Cosine Similarity  
Digunakan untuk mengukur kedekatan antara dua anime dalam ruang fitur. Nilainya berkisar antara 0 hingga 1, di mana semakin tinggi nilainya, semakin mirip dua anime tersebut.

Rumus:

$$
\text{Cosine Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \, \|\mathbf{B}\|}
$$

#### Keterangan:
- $\mathbf{A}, \mathbf{B}$: Vektor fitur dari dua anime
- $\cdot$: Operasi *dot product* antara vektor $\mathbf{A}$ dan $\mathbf{B}$
- $\|\mathbf{A}\|, \|\mathbf{B}\|$: Magnitudo (panjang) dari masing-masing vektor



####  Contoh Output Rekomendasi  
Misalnya, pengguna menyukai anime *"Naruto"*, maka sistem memberikan rekomendasi Top-5 anime berikut:

| Peringkat | Judul Anime           | Alasan Rekomendasi                                      |
|-----------|------------------------|----------------------------------------------------------|
| 1         | Naruto Shippuden       | Lanjutan langsung dari seri utama                       |
| 2         | Fullmetal Alchemist    | Genre Action & Adventure yang serupa                     |
| 3         | Bleach                 | Tema action dan dunia supranatural                      |
| 4         | One Piece              | Petualangan epik dengan alur menarik                    |
| 5         | My Hero Academia        | Genre superhero dengan relevansi tema                     |

---

### 2. K-Nearest Neighbors (KNN) – Baseline Model

Algoritma KNN digunakan sebagai baseline untuk memprediksi skor anime berdasarkan kesamaan dengan anime-anime terdekat.

#### Rumus Jarak (Euclidean Distance)
Untuk menentukan tetangga terdekat, KNN menggunakan jarak Euclidean:

Rumus:

$$
\text{Euclidean Distance} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + \cdots + (z_1 - z_2)^2}
$$

#### Keterangan:
- $x_1, y_1, \dots, z_1$: Komponen dari vektor pertama
- $x_2, y_2, \dots, z_2$: Komponen dari vektor kedua
- $\sqrt{\cdot}$: Akar kuadrat dari jumlah kuadrat selisih komponen-komponen vektor
- Simbol $\cdots$ menunjukkan penjumlahan untuk semua dimensi vektor yang ada


#### Parameter Utama:
- `n_neighbors = 5`
- Menggunakan data gabungan dari matriks fitur (`combined_sparse`) dan skor ternormalisasi

#### Kelebihan:
- Sederhana dan mudah dipahami.
- Tidak memerlukan pelatihan kompleks.
- Cocok untuk dataset yang sudah direpresentasikan secara numerik.

#### Kekurangan:
- Sensitif terhadap skala data → perlu scaling fitur.
- Lambat pada dataset besar karena harus menghitung jarak ke semua item.
- Hasil tidak stabil jika data sedikit atau banyak duplikasi konten.

---

### 3. Random Forest Regressor – Model Terbaik

Random Forest digunakan untuk memprediksi skor anime berdasarkan fitur-fitur konten dan metadata. Sebagai ensemble method, model ini melatih banyak pohon keputusan dan menggabungkan hasilnya untuk meningkatkan stabilitas dan akurasi.

#### Rumus Prediksi (Aggregation of Trees)
Prediksi akhir diperoleh dari rata-rata hasil dari seluruh pohon:

### Rumus:

ŷ = (1 / T) * Σ ŷₜ

### Keterangan:
- T: Jumlah pohon dalam Random Forest
- ŷₜ: Prediksi dari pohon ke-t
- ŷ: Prediksi akhir model, diperoleh dari rata-rata semua prediksi pohon


#### Parameter Utama:
- `n_estimators = 100`
- `random_state = 42`

#### Kelebihan:
- Stabil dan tahan overfitting dibandingkan KNN.
- Mampu menangkap hubungan non-linear antar fitur.
- Memberikan performa terbaik dengan RMSE = **0.0096** dan R² = **0.9999**.

#### Kekurangan:
- Lebih sulit diinterpretasi dibanding model tunggal.
- Waktu pelatihan lebih lama daripada model sederhana.

---

### 4. Gradient Boosting Regressor – Alternatif Kuat

Gradient Boosting juga digunakan untuk memprediksi skor anime. Teknik ini membangun model secara bertahap dengan fokus pada error dari model sebelumnya.

#### Rumus Pembaruan Model (Boosting Iteratif)
### Rumus:

Fₘ(x) = Fₘ₋₁(x) + η · hₘ(x)

### Keterangan:
- Fₘ(x): Model pada iterasi ke-m
- Fₘ₋₁(x): Model pada iterasi sebelumnya
- η: Learning rate (mengatur seberapa besar kontribusi pembaruan)
- hₘ(x): Weak learner (decision tree) pada iterasi ke-m


#### Parameter Utama:
- `n_estimators = 100`
- `random_state = 42`

#### Kelebihan:
- Sangat akurat dalam memprediksi skor anime.
- Mampu menangani interaksi antar fitur dengan baik.
- Performa mendekati Random Forest.

#### Kekurangan:
- Rentan overfitting jika tidak ditune dengan benar.
- Memerlukan tuning parameter yang lebih teliti.
- Waktu pelatihan sedikit lebih lama dari Random Forest.

---

### 5. Evaluasi dan Pemilihan Model Terbaik

Evaluasi dilakukan menggunakan dua metrik utama:
- **RMSE (Root Mean Squared Error)**: Mengukur kesalahan rata-rata prediksi.
- **R² Score**: Mengukur seberapa besar variasi target bisa dijelaskan oleh model.

Hasil evaluasi:

| Model                     | RMSE        | R² Score   |
|--------------------------|-------------|------------|
| KNN                      | 0.5745      | 0.6118     |
| Random Forest Regressor  | **0.0096**  | **0.9999** |
| Gradient Boosting Regressor | 0.0113    | 0.9998     |

#### Interpretasi:
- **Random Forest Regressor** menjadi model terbaik karena mampu memprediksi skor anime dengan sangat presisi.
- **Gradient Boosting** juga memberikan hasil yang sangat baik, menjadikannya alternatif yang layak.
- **KNN** memiliki performa paling rendah, sehingga tidak disarankan sebagai model utama.
  
---
### 6.  Hasil Rekomendasi Model Terbaik
Berikut adalah hasil rekomendasi berbasis konten (*content-based filtering*) menggunakan cosine similarity untuk judul `"Naruto"`:

| No | Judul Anime                                      | Score  | Genres                                | Similarity |
|----|--------------------------------------------------|--------|----------------------------------------|------------|
| 1  | Naruto: Shippuden                               | 8.26   | Action, Adventure, Fantasy              | 0.9826     |
| 2  | Boruto: Naruto Next Generations                  | 6.06   | Action, Adventure, Fantasy              | 0.9767     |
| 3  | One Piece                                       | 8.69   | Action, Adventure, Fantasy              | 0.9708     |
| 4  | Hunter x Hunter (2011)                           | 9.04   | Action, Adventure, Fantasy              | 0.9708     |
| 5  | Nanatsu no Taizai                                 | 7.67   | Action, Adventure, Fantasy              | 0.9707     |
| 6  | Bleach                                          | 7.92   | Action, Adventure, Fantasy              | 0.9703     |
| 7  | Nanatsu no Taizai: Imashime no Fukkatsu         | 7.59   | Action, Adventure, Fantasy              | 0.9698     |
| 8  | Fairy Tail                                     | 7.57   | Action, Adventure, Fantasy              | 0.9695     |
| 9  | Dungeon ni Deai wo Motomeru no wa Machigatteiru… | 7.55   | Action, Adventure, Fantasy              | 0.9692     |
| 10 | Log Horizon                                      | 7.93   | Action, Adventure, Fantasy              | 0.9682     |

>  *Keterangan*:  
- **Score**: Skor rata-rata dari komunitas MyAnimeList.
- **Genres**: Genre utama dari anime tersebut.
- **Similarity**: Nilai kemiripan konten terhadap *"Naruto"* menggunakan metrik *cosine similarity* (semakin mendekati 1, semakin mirip).

---

### 7. Analisis Hasil Rekomendasi

Hasil menunjukkan bahwa:
- **Top rekomendasi** adalah *Naruto: Shippuden*, sebagai lanjutan langsung dari seri utama, memiliki genre dan alur cerita sangat serupa.
- **One Piece**, **Hunter x Hunter (2011)**, dan **Bleach** juga masuk dalam daftar karena kesamaan genre seperti *Action*, *Adventure*, dan *Fantasy*.
- Semua anime dalam daftar memiliki elemen aksi dan petualangan, menjadikannya relevan secara kontekstual untuk penggemar *Naruto*.
- Meskipun beberapa anime memiliki skor lebih tinggi dari *Naruto*, sistem berhasil merekomendasikan anime yang benar-benar sesuai preferensi genre dan tema.

---

### **Kelebihan dan Kekurangan Pendekatan yang Dipilih**

| Model/Approach                        | Kelebihan                                                                 | Kekurangan                                                  |
|--------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------|
| Content-Based Filtering                | - Tidak memerlukan data interaksi pengguna<br>- Cocok untuk cold-start user    | - Tidak bisa merekomendasikan anime baru tanpa konten lengkap  |
| Random Forest Regressor               | - Akurasi tinggi<br>- Stabil dan resisten terhadap overfitting              | - Rentan terhadap noise jika tidak diproses dengan benar      |
| KNN                                  | - Sederhana<br>- Mudah dipahami                                            | - Sensitif terhadap skala data<br>- Lambat pada dataset besar |
| Gabungan CBF + Prediksi Skor         | - Meningkatkan personalisasi rekomendasi                                   | - Lebih kompleks                                             |

---
## Evaluation

Pada tahap ini dilakukan evaluasi terhadap model sistem rekomendasi yang telah dibangun. Evaluasi bertujuan untuk memastikan bahwa rekomendasi yang diberikan relevan dan sesuai dengan preferensi pengguna. Berikut adalah metrik evaluasi yang digunakan serta hasil yang dicapai:

### 1. Metrik Evaluasi

#### a. **RMSE (Root Mean Squared Error)**
- Digunakan untuk mengevaluasi akurasi model regresi yang memprediksi skor anime.
- Semakin rendah nilai RMSE, semakin baik prediksi dari model tersebut.

### Rumus:

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$



#### Keterangan:
- $n$: Jumlah total data/pengamatan  
- $y_i$: Nilai aktual (ground truth) pada data ke-$i$  
- $\hat{y}_i$: Nilai prediksi dari model pada data ke-$i$  
- $\sum$: Simbol penjumlahan dari $i = 1$ hingga $n$  
- RMSE (**Root Mean Squared Error**) adalah metrik yang mengukur rata-rata besarnya kesalahan antara nilai prediksi dan nilai aktual dalam satuan yang sama dengan data aslinya.  
- Semakin kecil nilai RMSE, semakin akurat model dalam melakukan prediksi.


#### b. **R² Score (Koefisien Determinasi)**
- Mengukur seberapa besar variasi target (`Score`) dapat dijelaskan oleh model.
- Nilainya berkisar antara 0 hingga 1, dimana semakin mendekati 1 menunjukkan kemampuan model menjelaskan data semakin tinggi.

#### Rumus:

# R² = 1 − (∑(yᵢ − ŷᵢ)²) / (∑(yᵢ − ȳ)²)

#### Keterangan:
- $n$: Jumlah data pengamatan
- $y_i$: Nilai aktual pada data ke-$i$
- $\hat{y}_i$: Nilai prediksi model pada data ke-$i$
- $\bar{y}$: Rata-rata nilai aktual seluruh data
- $\sum$: Simbol penjumlahan dari $i=1$ sampai $n$
- Pembilang ($\sum (y_i - \hat{y}_i)^2$) adalah jumlah kuadrat error prediksi (Residual Sum of Squares, RSS)
- Penyebut ($\sum (y_i - \bar{y})^2$) adalah total variasi data aktual terhadap rata-rata (Total Sum of Squares, TSS)
- Nilai $R^2$ berkisar antara 0 sampai 1, semakin mendekati 1 menunjukkan model semakin baik dalam menjelaskan variabilitas data

### 2. Hasil Evaluasi Model Regresi

Tiga model pembelajaran mesin diuji coba untuk memprediksi skor anime berdasarkan fitur konten:

| Model                     | RMSE        | R² Score   |
|--------------------------|-------------|------------|
| KNN                      | 0.5745      | 0.6118     |
| Random Forest Regressor  | **0.0096**  | **0.9999** |
| Gradient Boosting Regressor | 0.0113    | 0.9998     |

#### Interpretasi:
- **Random Forest Regressor** memberikan performa terbaik dengan **RMSE = 0.0096** dan **R² = 0.9999**, menunjukkan bahwa model ini mampu memprediksi skor anime secara sangat akurat.
- **Gradient Boosting Regressor** juga menunjukkan kinerja yang sangat baik, hanya sedikit di bawah Random Forest.
- **KNN** memiliki performa paling rendah karena sensitivitas pada skala data dan kurang efektif pada dataset sparse.

---

## 3. Visualisasi Hasil Evaluasi

### 3.1 **Bar Chart: RMSE per Model**

![RMSE per Model](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/Metriks%20Evaluasi.png)

#### Insight:
- Random Forest memiliki RMSE terkecil → kesalahan prediksi terendah.
- KNN memiliki RMSE tertinggi → kurang tepat untuk prediksi skor anime.

---

### 3.2 **Bar Chart: R² Score per Model**

![R² Score per Model](https://github.com/Reswn/Anime-Recomendation-System/blob/main/src/R2%20Score.png)

#### Insight:
- R² score Random Forest mendekati 1 → model ini mampu menjelaskan hampir seluruh variasi data.
- Hal ini membuktikan bahwa Random Forest sangat layak digunakan dalam sistem rekomendasi.

---

### Kesimpulan

Berdasarkan evaluasi menggunakan **RMSE** dan **R² Score**, serta validasi manual rekomendasi:

- **Random Forest Regressor** menjadi model terbaik dengan **RMSE = 0.0096** dan **R² = 0.9999**, menunjukkan bahwa model ini mampu memprediksi skor anime dengan sangat akurat.
- **Content-Based Filtering** berhasil memberikan rekomendasi berdasarkan kedekatan konten dan genre.
- Hasil rekomendasi ditingkatkan dengan pendekatan **hybrid**: gabungan antara kemiripan konten dan prediksi skor anime.

Meskipun belum melibatkan data interaksi pengguna, sistem ini sudah cukup kuat untuk digunakan oleh pengguna baru atau sebagai fitur pencarian berbasis konten.

---

---

### Referensi

[5] J.M. Ph.D dan E. Kavlakoglu, "Content-based filtering," IBM, 2024. [Online]. Available: https://www.ibm.com/think/topics/content-based-filtering

[2] GeeksforGeeks, "K-Nearest Neighbor(KNN) Algorithm," 2017. [Online]. Available: https://www.geeksforgeeks.org/k-nearest-neighbours/

[3] GeeksforGeeks, "Random Forest Algorithm in Machine Learning," 2024. [Online]. Available: https://www.geeksforgeeks.org/random-forest-algorithm-in-machine-learning/

[4] GeeksforGeeks, "Gradient Boosting in ML," 2020. [Online]. Available: https://www.geeksforgeeks.org/ml-gradient-boosting/

---

