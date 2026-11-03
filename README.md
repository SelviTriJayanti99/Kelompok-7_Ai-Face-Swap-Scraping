# Analisis Komentar Twitter/X: Isu Rupiah Melemah

Project ini mengolah ekspor komentar Twitter/X yang membahas pelemahan nilai tukar rupiah terhadap dolar AS. Data dibersihkan dengan Python, lalu diringkas untuk melihat siapa yang berkomentar, kapan, dan apa yang diramaikan.

## 1. Latar Belakang Topik

Nilai tukar rupiah adalah salah satu indikator ekonomi yang paling cepat memancing reaksi publik. Ketika rupiah melemah, dampaknya terasa pada harga barang impor, biaya produksi, utang luar negeri, sampai kepercayaan investor. Karena itu isu ini selalu ramai dibahas di media sosial, terutama Twitter/X.

Pelemahan rupiah yang paling banyak dibicarakan terjadi pada awal April 2025. Menurut pemberitaan Bisnis.com, pada 8 April 2025 rupiah di pasar spot menyentuh sekitar Rp16.845 per dolar AS, level terlemah sejak krisis keuangan 1998. Setelah itu rupiah sempat tembus sekitar Rp17.000, dan Bank Dunia dalam laporan Global Economic Prospects Juni 2025 menyebut tekanan itu berkaitan dengan ketidakpastian kebijakan dalam negeri.

Di Twitter/X, angka-angka ini langsung diterjemahkan menjadi opini: ada yang menyalahkan kebijakan fiskal dan impor, ada yang mengaitkannya dengan pernyataan pejabat, ada yang membandingkannya dengan krisis 1998. Pola ini membuat kolom komentar menjadi sumber data yang menarik untuk melihat bagaimana publik merespons isu ekonomi.

## 2. Alasan Mengganti Topik dari AI Face Swap ke Rupiah Melemah

Topik awal project ini adalah AI face swap. Topik tersebut diganti karena pembahasannya didominasi pengguna dari luar negeri, sedangkan percakapan dari pengguna Indonesia sangat sedikit. Akibatnya data yang bisa dikumpulkan kurang mewakili konteks Indonesia dan sulit dianalisis sebagai data berbahasa Indonesia.

Karena itu dipilih topik baru yang lebih banyak dibicarakan di Indonesia, yaitu rupiah melemah. Hasilnya terlihat pada dataset: dari 1.519 komentar, 1.312 (86,4%) berbahasa Indonesia. Isu ini juga dekat dengan bidang ekonomi dan bisnis, dan muncul berulang pada lima periode (2018, 2020, Desember 2024, April 2025, Juni 2026).

Beberapa alasan pergantian topik tersebut adalah:

- **Relevansi isu:** Fenomena melemahnya rupiah merupakan permasalahan ekonomi yang berkaitan langsung dengan kondisi Indonesia dan kehidupan masyarakat.
- **Ketersediaan data:** Topik ini memiliki banyak pembahasan dan tanggapan pengguna di platform X sehingga dapat dimanfaatkan sebagai sumber data.
- **Potensi analisis:** Komentar masyarakat memiliki beragam pandangan yang dapat dianalisis untuk mengetahui kecenderungan opini dan sentimen.
- **Fokus penelitian:** Topik baru dinilai lebih sesuai untuk melakukan pengumpulan data dan analisis terhadap respons masyarakat mengenai suatu fenomena.

## 3. Pembagian Tugas Kelompok

| Anggota | Tugas |
|---|---|
| Selvi Tri Jayanti | Bertanggung jawab dalam proses pengumpulan data menggunakan platform Apify. |
| Miskatul Jannah | Membantu mencari dan mengidentifikasi tautan unggahan Twitter/X yang membahas fenomena Rupiah Melemah. |
| Azika Adzahila | Bertanggung jawab atas proses scraping untuk mengumpulkan komentar dari postingan yang telah ditentukan. |

## 4. Struktur Folder

```text
twitter_comments_project/
├── data/
│   ├── raw/
│   │   └── dataset_twitter_comments.csv
│   └── processed/
│       └── twitter_comments_clean.csv  # dibuat setelah cleaning
├── clean_data.py
├── analyze_data.py
├── requirements.txt
└── README.md
```

## 5. Cara Menjalankan

Buka folder `twitter_comments_project` di VS Code, lalu di Terminal jalankan:

```bash
python -m pip install -r requirements.txt   # persiapan
python clean_data.py                        # membersihkan data
python analyze_data.py                      # melihat ringkasan data
```

`clean_data.py` mengambil kolom yang relevan, merapikan teks komentar, mengubah metrik interaksi menjadi angka, menghapus komentar kosong dan duplikat, lalu menyimpan hasilnya ke `data/processed/twitter_comments_clean.csv`. File mentah tidak diubah.

`analyze_data.py` menampilkan jumlah komentar, distribusi bahasa, rata-rata interaksi, akun yang paling sering muncul, dan contoh komentar.

## 6. Penjelasan Hasil Scraping

### 6.1 Gambaran umum dataset

| Item | Hasil |
|---|---|
| Jumlah komentar | 1.519 baris, 11 kolom |
| Akun unik | 1.426 |
| Rentang waktu | 16 Mei 2018 sampai 14 Juli 2026 |
| Bahasa dominan | Indonesia (`in`) 1.312 komentar atau 86,4%, lalu Inggris 66, `qme` 57, Tagalog 22, tidak terdeteksi 15, Turki 7 |
| Panjang komentar | median 62 karakter, rata-rata sekitar 89 karakter |
| Data kosong | hanya kolom `views` (239 baris, 15,7%) |

Kolom yang tersedia: `platform`, `comment_id`, `created_at`, `username`, `comment`, `language`, `likes`, `replies`, `retweets`, `quotes`, `views`.

Nilai `views` yang kosong seluruhnya (kecuali 3 baris) berasal dari komentar tahun 2018 dan 2020, kemungkinan karena metrik views belum ditampilkan Twitter/X pada masa itu.

### 6.2 Komentar mengelompok pada lima periode

Komentar tidak tersebar merata, tetapi mengumpul sebagai balasan pada beberapa cuitan tertentu:

| Periode | Jumlah | Balasan pada cuitan | Catatan |
|---|---|---|---|
| Mei 2018 | 93 | @fadlizon | Balasan yang juga menandai @jokowi |
| April 2020 | 143 | @budimandjatmiko | Sebagian komentar membahas rupiah yang menguat |
| Desember 2024 | 329 | @BigAlphaID | Rupiah di kisaran Rp16.000-an, banyak yang menyebut angka kurs dan krisis 1998 |
| April 2025 | 544 | @investorgabut (339), @AlwaysBeenChoze (179), lainnya | Periode rupiah menyentuh rekor terlemah; komentar banyak membahas impor, kebijakan, dan investor asing |
| Juni sampai Juli 2026 | 410 | @tempedotc0 (364) | Banyak komentar mengaitkan pelemahan rupiah dengan pidato presiden |

Artinya dataset ini bukan sampel acak dari seluruh percakapan tentang rupiah. Ia adalah kumpulan balasan pada beberapa cuitan yang kebetulan banyak direspons.

### 6.3 Interaksi sangat timpang

- Median likes, replies, retweets, dan quotes semuanya 0. Hanya sekitar seperempat komentar yang mendapat lebih dari 1 like.
- Rata-rata likes 11,7, tetapi nilai maksimumnya 2.360. Artinya sebagian kecil komentar mengambil hampir semua perhatian.
- Total likes terbesar ada pada April 2025 (11.032 dari total 17.788, sekitar 62%), diikuti Juni 2026 (3.154).
- Komentar dengan likes tertinggi berisi sindiran terhadap kebijakan impor dan pidato presiden.

### 6.4 Akun dan kata yang menonjol

- Akun yang paling sering muncul adalah @tempedotc0 (43 kali) dan @AlwaysBeenChoze (23 kali). Keduanya adalah pemilik cuitan yang ikut membalas di kolom komentarnya sendiri. Akun lain muncul paling banyak 3 kali.
- Kata bermakna yang sering muncul antara lain `rupiah`, `presiden`, `impor`, `negara`, `ekonomi`, `pidato`, `asing`, `rakyat`, `pemerintah`, dan `kebijakan`. Kata `impor` terutama muncul di komentar April 2025, sedangkan `pidato` muncul di komentar 2026.
- Hanya 2 komentar yang teksnya duplikat, dan tidak ada `comment_id` ganda.

## 7. Kesimpulan

1. Dataset berisi 1.519 komentar Twitter/X yang sebagian besar (86,4%) berbahasa Indonesia, sehingga cocok untuk analisis teks berbahasa Indonesia.
2. Komentar mengelompok pada lima periode, dan puncaknya April 2025 (544 komentar, 35,8%), bertepatan dengan rupiah menyentuh rekor terlemah sejak krisis 1998.
3. Dari pembacaan contoh komentar, nada yang dominan adalah kritik terhadap pemerintah. Topik yang sering muncul adalah kebijakan impor, kepercayaan investor asing, dan pidato presiden. Bagian ini masih berdasarkan pembacaan sampel, belum hasil analisis sentimen.
4. Interaksi terkonsentrasi pada segelintir komentar. Sebagian besar komentar hampir tidak mendapat respons, sehingga rata-rata likes tidak mewakili komentar pada umumnya. Median lebih tepat dipakai.

## Sumber Latar Belakang

- Bisnis.com, "Rupiah Sentuh Rp16.845 per Dolar AS di Pasar Spot, Rekor Terburuk Sejak Krisis 1998" (8 April 2025).
- Investortrust.id, "Rupiah Sempat Tembus Rp 17.000 pada Awal April 2025, Bank Dunia Punya Analisis Ini" (Juni 2025).
