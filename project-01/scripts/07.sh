#!/bin/bash

source ./config.sh

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
