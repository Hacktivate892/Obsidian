# Obsidian

Obsidian is a simple custom programming language built using Bash. It uses a `.txt` file to store source code, which is interpreted and executed by a Bash-based interpreter.

The project is currently in its early stages, focusing on implementing basic programming functionality.

## Features

- Custom `.txt` source files
- Variable declaration using `var`
- Output using `print`
- Basic variable management
- Bash-based interpreter

## Project Structure

```text
Obsidian/
├── main.sh
├── variable.sh
└── program.txt
```

- `main.sh` - Main interpreter responsible for reading and executing code.
- `variable.sh` - Handles variable management.
- `program.txt` - Contains the source code written in Obsidian.

## Example Code

```text
var username = User2
var age = 15
var language = Obsidian

print username
print age
print language
```

## Running Obsidian

1. Clone the repository.
2. Open a terminal in the project directory.
3. Run the interpreter:

```bash
bash main.sh program.txt
```

## Development

Obsidian is actively being developed. More features, commands, and data types are planned as the interpreter evolves.

## Technologies

- Bash
- Git
- Visual Studio Code

## License

This project is currently under development.
