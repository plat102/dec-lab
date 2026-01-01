#!/bin/bash

source ./config.sh
OUTPUT_FILE="$OUTPUT_DIR/01_sorted_by_date.csv"

# ---------- Sub-task 1: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới ----------
echo "[1/8]: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới"

# 1. Lấy header trước
head -n 1 "$RAW_FILE" > "$OUTPUT_FILE"

# 2. Xử lí nội dung data: tạo cột phụ sửa format cột -> sort -> append
COL_RELEASE_DATE=16
(tail -n +2 "$RAW_FILE" | \
  sort -t',' -k${COL_RELEASE_DATE}.7,${COL_RELEASE_DATE}.8 \
             -k${COL_RELEASE_DATE}.1,${COL_RELEASE_DATE}.1 \
             -k${COL_RELEASE_DATE}.4,${COL_RELEASE_DATE}.5 -r)  \
>> "$OUTPUT_FILE"

echo "Done. Check result:"
head -n 5 "$OUTPUT_FILE"

