# Script này xử lý CSV có dấu phẩy nằm trong ngoặc kép (quoted commas).
# Logic: Tạm thay thế dấu phẩy (,) bên trong ngoặc kép thành <comma>
# Ref: https://stackoverflow.com/questions/4205431/parse-a-csv-using-awk-and-ignoring-commas-inside-a-field

BEGIN {
    # Cắt chuỗi dựa trên dấu ngoặc kép "
    FS = "\""
    OFS = "\""
}

{
    # Duyệt qua các cột chẵn (ndung trong ngoặc)
    for (i = 2; i <= NF; i += 2) {
        # Thay thế tất cả dấu , thành <comma>
        gsub(",", "<comma>", $i)

        # Thay \n
        gsub("\n", " ", $i)

    }
    print $0
}