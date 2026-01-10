#!/bin/bash

source ./config.sh

echo "[4/8]: Tính tổng doanh thu tất cả các bộ phim (adjusted)"

tail -n +2 "$RAW_FILE" | \
awk -f ./scripts/clean_csv.awk | \
awk -F, '{
  total_revenue=total_revenue+$(NF)
}
END {
  print("--------------------------------------------------")
  printf("%\047d\n", total_revenue)
}
'
