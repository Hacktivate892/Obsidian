
#!/bin/bash

echo "Interpreter started!"

source "$(dirname "$0")/variable.sh"

if [[ ! -f "$1" ]]; then
    echo "Error: Program file not found!"
    exit 1
fi

while IFS= read -r line || [[ -n "$line" ]]; do

    echo "Reading: $line"

    if [[ "$line" =~ ^var[[:space:]]+([a-zA-Z_][a-zA-Z0-9_]*)[[:space:]]*=[[:space:]]*(.*)$ ]]; then
        declare_variable "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}"

    elif [[ "$line" =~ ^print[[:space:]]+([a-zA-Z_][a-zA-Z0-9_]*)$ ]]; then
        print_variable "${BASH_REMATCH[1]}"

    elif [[ -z "$line" || "$line" == \#* ]]; then
        continue

    else
        echo "Syntax Error: $line"
    fi

done < "$1"

echo "Interpreter finished!"
