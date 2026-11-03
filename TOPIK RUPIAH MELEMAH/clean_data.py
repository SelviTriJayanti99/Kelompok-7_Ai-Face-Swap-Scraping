import os
import glob
import pandas as pd

def clean_and_merge_twitter_data():
    # Cari semua file CSV di dalam folder data/raw
    search_path = os.path.join("data", "raw", "*.csv")
    csv_files = glob.glob(search_path)
    
    if not csv_files:
        print("Tidak ada file CSV ditemukan di folder data/raw.")
        return

    print(f"Ditemukan {len(csv_files)} file CSV di folder raw. Menggabungkan...")
    
    # Baca dan gabungkan semua file CSV
    df_list = []
    for file in csv_files:
        try:
            temp_df = pd.read_csv(file)
            df_list.append(temp_df)
            print(f" - Membaca: {os.path.basename(file)} ({len(temp_df)} baris)")
        except Exception as e:
            print(f" - Gagal membaca {file}: {e}")

    if not df_list:
        print("Tidak ada data yang berhasil dibaca.")
        return

    # Gabungkan semua dataframe dan buang duplikat
    df = pd.concat(df_list, ignore_index=True)
    before_dedup = len(df)

    # Tambahkan kolom platform agar persis seperti format TikTok
    df['platform'] = 'Twitter'

    # Pemetaan kolom
    column_mapping = {
        'id': 'comment_id',
        'created_at': 'created_at',
        'author/screen_name': 'username',
        'text': 'comment',
        'lang': 'language',
        'public_metrics/like_count': 'likes',
        'public_metrics/reply_count': 'replies',
        'public_metrics/retweet_count': 'retweets',
        'public_metrics/quote_count': 'quotes',
        'public_metrics/bookmark_count': 'views'
    }

    df = df.rename(columns=column_mapping)

    target_columns = [
        'platform', 'comment_id', 'created_at', 'username', 'comment',
        'language', 'likes', 'replies', 'retweets', 'quotes', 'views'
    ]
    
    available_columns = [col for col in target_columns if col in df.columns]
    clean_df = df[available_columns].drop_duplicates()

    # Simpan hasil akhir ke folder processed
    PROCESSED_DATA_PATH = os.path.join("data", "processed", "twitter_comments_clean.csv")
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    clean_df.to_csv(PROCESSED_DATA_PATH, index=False, encoding='utf-8')

    print("\nPROSES GABUNG & CLEANING DATA SELESAI")
    print("=" * 55)
    print(f"Total data mentah digabung : {before_dedup}")
    print(f"Jumlah data bersih akhir   : {len(clean_df)}")
    print(f"File hasil                 : {os.path.abspath(PROCESSED_DATA_PATH)}")

if __name__ == "__main__":
    clean_and_merge_twitter_data()