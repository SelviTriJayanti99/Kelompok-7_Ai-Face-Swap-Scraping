"""
Ringkasan sederhana dataset komentar Twitter/X.
Jalankan:
    python analyze_data.py
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "processed" / "twitter_comments_clean.csv"

def main():
    if not DATA_FILE.exists():
        print("File bersih belum ada. Jalankan: python clean_data.py")
        return

    df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
    print("\n========== RINGKASAN DATA ==========")
    print(f"Total komentar : {len(df)}")
    print(f"Total kolom    : {len(df.columns)}")

    if "lang" in df.columns:
        print("\nBahasa komentar:")
        print(df["lang"].value_counts().head(10).to_string())

    metrics = [c for c in ["likes", "replies", "retweets", "quotes", "views"] if c in df.columns]
    if metrics:
        print("\nRata-rata interaksi:")
        print(df[metrics].mean().round(2).to_string())

    if "author/screen_name" in df.columns:
        print("\nAkun paling sering muncul:")
        print(df["author/screen_name"].value_counts().head(10).to_string())

    print("\nContoh komentar:")
    print(df["comment"].head(5).to_string(index=False))

if __name__ == "__main__":
    main()
