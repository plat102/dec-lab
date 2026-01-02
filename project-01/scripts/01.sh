#!/bin/bash

# NOTE: cần so sánh kết quả với cách 2

source ./config.sh
OUTPUT_FILE="$OUTPUT_DIR/01_sorted_by_date.csv"

echo "[1/8]: Sắp xếp các bộ phim theo ngày phát hành giảm dần rồi lưu ra một file mới"

# 1. Header
head -n 1 "$RAW_FILE" | awk '{print "release_date_parsed," $0}' > "$OUTPUT_FILE"

# 2. Xử lý Data
# Clean CSV -> Xử lý data -> Sort -> Output
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, -v OFS=',' '{
    raw_date = $16

    # --- Logic xử lý ngày tháng ---
    split(raw_date, d, "/")
    if (length(d) == 3) {
        year = (d[3] < 50 ? "20" d[3] : "19" d[3])
        parsed_date = sprintf("%s-%02d-%02d", year, d[1], d[2])
    } else {
        parsed_date = "1900-01-01"
    }

    # --- Trả dấu phẩy (Optional) ---
    # gsub("<comma>", ",", $0)

    print parsed_date, $0
}' | \
sort -t, -k1r >> "$OUTPUT_FILE"

echo "Done. Check result:"
tail -n 5 "$OUTPUT_FILE"