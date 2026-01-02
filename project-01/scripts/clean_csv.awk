BEGIN {
    EXPECTED_COLS = 21  # Dataset num of cols
}

{
    sub(/\r$/, "", $0)

    # --- Accumulate buffer (line) for line full content
    if (buffer != "") {
        buffer = buffer " " $0
    } else {
        buffer = $0
    }

    # --- Check 1: even # of quotes
    temp = buffer
    count_quote = gsub("\"", "\"", temp)
    # If even, quote may closed
    if (count_quote % 2 == 0) {
        # --- Transform quoted content
        n = split(buffer, parts, "\"")
        final_line = ""

        for (i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                # Replace comma & newline
                gsub(/,/, "<comma>", parts[i])
                gsub(/\n/, " ", parts[i])
            }
            final_line = final_line parts[i]
            if (i < n) final_line = final_line "\""
        }

        # --- Check 2: columns >= 21
        if (split(final_line, trash, ",") >= EXPECTED_COLS) {
            print final_line
            buffer = ""
        }
    }
    # Keep buffer
}