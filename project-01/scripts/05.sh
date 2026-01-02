#!/bin/bash

source ./config.sh

TMP_FILE="$OUTPUT_DIR/temp_profit.csv"

echo "[5/8]: Top 10 bộ phim đem về lợi nhuận cao nhất"

# B1: Clean CSV -> File tạm
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    gsub("<comma>", ",", $6)

    # Title | Profit (Revenue - Budget)
    print $6 "|" ($5 - $4)
}' > "$TMP_FILE"

# B2: In ra top 10
echo "-----------------------------------------------------------------"
sort -t'|' -k2nr "$TMP_FILE" | head -n 10 | \
awk -F'|' '{
  printf("%50s | %s\n", $1, $2)
}'