import csv, glob, hashlib

rows, seen = [], set()
for f in glob.glob("data/raw/*.csv"):
    with open(f, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            cid = r.get("cid")
            text = (r.get("text") or "").strip()
            if not cid or cid in seen or not text:
                continue
            seen.add(cid)
            rows.append({
                "platform": "TikTok",
                "comment_id": cid,
                "created_at": r.get("createTimeISO"),
                "username": hashlib.md5(
                    (r.get("uniqueId") or "").encode()).hexdigest()[:8],
                "comment": text,
                "likes": r.get("diggCount"),
                "replies": r.get("replyCommentTotal"),
                "video_url": r.get("videoWebUrl"),
            })

with open("data/tiktok_comments_clean.csv", "w",
          encoding="utf-8-sig", newline="") as out:
    w = csv.DictWriter(out, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

print(len(rows), "baris bersih")
for f in glob.glob("data/raw/*.csv"):
    with open(f, encoding="utf-8-sig", newline="") as fh:
        print(f, sum(1 for _ in csv.DictReader(fh)), "baris")