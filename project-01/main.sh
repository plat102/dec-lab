#!/bin/bash
source ./config.sh

# ---------- Explore data ----------
#wget -P ./data/raw/ https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv
cp ./data/raw/tmdb-movies.csv ./data/tmdb-movies.csv

echo "Raw file: $RAW_FILE"
# View file size (line, byte, max line length)
wc -lcL $RAW_FILE
# View columns
head -2 $RAW_FILE
tail -3 $RAW_FILE
# Count columns
echo
echo "Number of columns: $(head -1 $RAW_FILE | awk -F , '{print NF}')"

# ---------- 1 ----------
echo
source $SCRIPTS_DIR/01.sh

# ---------- 2 ----------


# ---------- 3 ----------