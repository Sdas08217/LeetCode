# Transose File
#!/bin/bash


# Define the input file
input_file="file.txt"

# Use awk to process the file and transpose it
awk '
{
    for (i = 1; i <= NF; i++) {
        # Store the field in a 2D array with swapped indices
        matrix[i, NR] = $i
    }
    # Keep track of the maximum number of fields (columns) and rows
    if (NF > max_fields) {
        max_fields = NF
    }
    max_rows = NR
}
END {
    for (i = 1; i <= max_fields; i++) {
        for (j = 1; j <= max_rows; j++) {
            # Print the transposed field with a space delimiter
            printf "%s%s", matrix[i, j], (j == max_rows ? "\n" : " ")
        }
    }
}
' $input_file
