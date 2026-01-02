#!/bin/bash

source ./config.sh

OUTPUT_FILE="$OUTPUT_DIR/02_filter_vote.csv"

echo "[2/8]: Lọc ra các bộ phim có đánh giá trung bình trên 7.5 rồi lưu ra một file mới"

# Header
head -n 1 "$RAW_FILE"  > "$OUTPUT_FILE"

# Append content
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, -v OFS=',' '{
  vote_avg = $18

  if ($18 > 7.5){
    print($0)
  }
}' >> "$OUTPUT_FILE"

echo "Done. Check result:"
head -n 5 "$OUTPUT_FILE"
