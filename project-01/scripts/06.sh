#!/bin/bash

source ./config.sh

echo "[6/8]: Đạo diễn nào có nhiều bộ phim nhất và diễn viên nào đóng nhiều phim nhất"

# ----------- Director -----------
echo "--- Đạo diễn: "
tail -n +2 "$RAW_FILE" | awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    # In từng đạo diễn mỗi phim ra 1 dòng
    n = split($9, arr, "|");
    for (i=1; i<=n; i++) print arr[i]
}' | \
sort | uniq -c | \
sort -nr | head -n 1

# ----------- Cast -----------
echo "--- Diễn viên: "
tail -n +2 "$RAW_FILE" | awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    n = split($7, arr, "|");
    for (i=1; i<=n; i++) print arr[i]
}' | \
sort | uniq -c | \
sort -nr | head -n 1
