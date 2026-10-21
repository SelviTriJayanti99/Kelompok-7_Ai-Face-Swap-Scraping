import csv

urls = {}

# Membaca data komentar
with open("data/tiktok_comments_clean.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        url = r["video_url"].strip()
        if url:
            urls[url] = urls.get(url, 0) + 1

# Menyimpan semua link video ke CSV
with open("tiktok_video_links.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["video_url", "jumlah_komentar"])

    for url, jumlah in sorted(urls.items(), key=lambda x: -x[1]):
        writer.writerow([url, jumlah])

print(f"Berhasil! Total {len(urls)} link video tersimpan.")
print("File: tiktok_video_links.csv")