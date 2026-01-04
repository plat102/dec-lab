#!/bin/bash
echo "Setting up env..."
RAW_FILE="./data/tmdb-movies.csv"
OUTPUT_DIR="./data/output"
SCRIPTS_DIR="./scripts"

# ---------- Explore data ----------
wget -P ./data/raw/ https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv
cp ./data/raw/tmdb-movies.csv ./data/tmdb-movies.csv

echo "Raw file: $RAW_FILE"
# View file size (line, byte, max line length)
wc -lcL $RAW_FILE
# View columns
#head -2 $RAW_FILE
#tail -3 $RAW_FILE
# Count columns
echo
echo "Number of columns (header): $(head -1 $RAW_FILE | awk -F , '{print NF}')"
awk -F, '{print NF}' $RAW_FILE | sort | uniq -c

# ---------- 1 ----------
echo
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
# ---------- 2 ----------
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

# ---------- 3 ----------
echo

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

# ---------- 4 ----------
echo
echo "[4/8]: Tính tổng doanh thu tất cả các bộ phim"

tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
  total_revenue=total_revenue+$5
}
END {
  print("--------------------------------------------------")
  printf("%\047d\n", total_revenue)
}
'

# ---------- 5 ----------
echo

TMP_FILE="$OUTPUT_DIR/temp_profit.csv"

echo "[5/8]: Top 10 bộ phim đem về lợi nhuận cao nhất"

# B1: Clean CSV -> File tạm
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    gsub("<comma>", ",", $6)

    rev = $5 + 0
    bud = $4 + 0

    if (rev > 0 && bud > 0) {
         printf "%s|%.0f\n", $6, (rev - bud)
    }
}' > "$TMP_FILE"

# B2: In ra top 10
echo "-----------------------------------------------------------------"
sort -t'|' -k2nr "$TMP_FILE" | head -n 10 | \
awk -F'|' '{
  printf("%50s | %s\n", $1, $2)
}'

# ---------- 6 ----------
echo

TMP_FILE="$OUTPUT_DIR/temp_profit_adj.csv"

echo "[5/8]: Top 10 bộ phim đem về lợi nhuận cao nhất (theo doanh thu & budget adjust)"

# B1: Clean CSV -> File tạm
tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    gsub("<comma>", ",", $6)

    # Title | Profit (Revenue - Budget)
    printf "%s|%.0f\n", $6, ($NF - $(NF-1))
}' > "$TMP_FILE"

# B2: In ra top 10
echo "-----------------------------------------------------------------"
sort -t'|' -k2nr "$TMP_FILE" | head -n 10 | \
awk -F'|' '{
  printf("%50s | %s\n", $1, $2)
}'

# ---------- 7 ----------
echo

echo "[7/8]: Thống kê số lượng phim theo các thể loại."

tail -n +2 "$RAW_FILE" | awk -f ./scripts/clean_csv.awk | \
awk -F, '{
    n = split($14, arr, "|");
    for (i=1; i<=n; i++){
      if (length(arr[i]) > 0) print arr[i]
    }
}' | \
sort | uniq -c | \
sort -nr

