#!/bin/bash

source ./config.sh
OUTPUT_FILE="$OUTPUT_DIR/01_sorted_by_date_2.csv"

# ---------- Sub-task 1: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới ----------
echo "[1/8]: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới"

# 1. Lấy header trước
head -n 1 "$RAW_FILE" | awk '{print "release_date_parsed," $0}' > "$OUTPUT_FILE"

# 2. Xử lí nội dung data:
# reverse index để tránh các cột text có data chứa ','
# tạo cột phụ sửa format cột -> sort -> append
tail -n +2 "$RAW_FILE" | awk -F',' -v OFS=',' '
{
  # Dòng trống
  if (NF < 6) {
    print "1900-01-01", $0
    next
  }

  raw_date = $(NF-5)
  split(raw_date, d, "/")
  if (length(d) == 3) {
    # Đoán năm: < 25 là 20xx, còn lại 19xx
    year = (d[3] < 25 ? "20" d[3] : "19" d[3])
    # Format YYYY-MM-DD
    parsed_date = sprintf("%s-%02d-%02d", year, d[1], d[2])
  } else {
    parsed_date = "1900-01-01"
  }

  print parsed_date, $0
}' | \
sort -t, -k1r \
>> "$OUTPUT_FILE"

echo "Done. Check result:"
tail -n 5 "$OUTPUT_FILE"
