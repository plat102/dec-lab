#!/bin/bash

source ./config.sh

TMP_FILE="$OUTPUT_DIR/temp_revenue.csv"

echo "[3/8]: Tìm ra phim nào có doanh thu cao nhất và doanh thu thấp nhất"

# B1: Clean CSV -> Lấy cột 5 (Rev) và 6 (Title) -> File tạm
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    gsub("<comma>", ",", $6)
    print $5 "|" $6
}' > "$TMP_FILE"

# B2: Tìm max & min
echo "--------------------------------------------------"

# Max/min = gtrị trên cùng của data temp (sau sort)
find_value_match='
    NR==1 {
        target = $1;
        printf " -> [Doanh thu: $%d] %s\n", $1, $2;
        next
    }
    $1 == target {
        printf " -> [Doanh thu: $%d] %s\n", $1, $2
    }
    $1 != target {
        exit
    }
'

echo "----- Phim có doanh thu CAO NHẤT:"
# -k1nr : sort cột 1 (Revenue), n=số, r=giảm dần
sort -t'|' -k1nr "$TMP_FILE" | awk -F'|' "$find_value_match"

echo ""
echo "----- Phim có doanh thu THẤP NHẤT:"
# lọc dthu > 0
awk -F'|' '$1 > 0' "$TMP_FILE" | \
sort -t'|' -k1n | awk -F'|' "$find_value_match"
