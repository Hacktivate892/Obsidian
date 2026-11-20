
#!/bin/bash

variable_names=()
variable_values=()

declare_variable() {
    local name="$1"
    local value="$2"
    local i

    if [[ ! "$name" =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
        echo "Error: Invalid variable name '$name'"
        return 1
    fi

    # Update existing variable or create a new one
    for i in "${!variable_names[@]}"; do
        if [[ "${variable_names[$i]}" == "$name" ]]; then
            variable_values[$i]="$value"
            return
        fi
    done

    variable_names+=("$name")
    variable_values+=("$value")
}

print_variable() {
    local name="$1"
    local i

    for i in "${!variable_names[@]}"; do
        if [[ "${variable_names[$i]}" == "$name" ]]; then
            echo "${variable_values[$i]}"
            return
        fi
    done

    echo "Error: Variable '$name' does not exist."
}
