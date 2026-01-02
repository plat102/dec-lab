#!/bin/bash
source ./config.sh

# ---------- Explore data ----------
#wget -P ./data/raw/ https://raw.githubusercontent.com/yinghaoz1/tmdb-movie-dataset-analysis/master/tmdb-movies.csv
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
source $SCRIPTS_DIR/01.sh
awk -F, '{print NF}' $OUTPUT_DIR/01_sorted_by_date.csv | sort | uniq -c

# ---------- 2 ----------
echo
source $SCRIPTS_DIR/02.sh


# ---------- 3 ----------
echo
source $SCRIPTS_DIR/03.sh

# ---------- 4 ----------
echo
source $SCRIPTS_DIR/04.sh

# ---------- 5 ----------
echo
source $SCRIPTS_DIR/05.sh

# ---------- 6 ----------
echo
source $SCRIPTS_DIR/06.sh

# ---------- 7 ----------
echo
source $SCRIPTS_DIR/07.sh
