"""
scrape_tiktok.py
Mengambil komentar TikTok bertopik AI face swap memakai Apify
(actor: TikTok Comments Scraper), lalu menyimpannya sebagai CSV mentah.
"""
import csv
import os
from apify_client import ApifyClient

# Token jangan ditulis asli di GitHub. Isi lewat environment variable
# APIFY_TOKEN, atau ganti placeholder ini hanya di laptopmu.
APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "ISI_APIFY_TOKEN")

ACTOR = "clockworks/tiktok-comments-scraper"

VIDEO_URLS = [
    "https://www.tiktok.com/@sebastienjefferies/video/7555782840592370966",
    "https://www.tiktok.com/@nsrltutorial/video/7669707415910124808",
    "https://www.tiktok.com/@eren.creates.ai/video/7626917778997382413",
    "https://www.tiktok.com/@davecthio/video/7554145292807982348",
    "https://www.tiktok.com/@eren.creates.ai/video/7635827320862870814",
    "https://www.tiktok.com/@gusti.gina/video/7608143771934526728",
]

run_input = {
    "postURLs": VIDEO_URLS,
    "commentsPerPost": 400,
}

client = ApifyClient(APIFY_TOKEN)
run = client.actor(ACTOR).call(run_input=run_input)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(len(items), "komentar mentah diambil")

os.makedirs("data/raw", exist_ok=True)
fieldnames = sorted({key for item in items for key in item})
with open("data/raw/tiktok_comments_raw.csv", "w",
          encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(items)

print("Tersimpan di data/raw/tiktok_comments_raw.csv")
