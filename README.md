# File Manager

A lightweight Python module for handling file I/O operations using an abstract base class (ABC) pattern. This provides a flexible interface for reading from and writing to files, with extensible methods for future enhancements.

## Features
- **Abstract Interface**: Uses `abc` module to define a `FileManager` base class with an `explore` method.
- **File Reader**: Implements reading file contents.
- **File Writer**: Implements writing content to files (with customizable modes).
- **UTF-8 Encoding**: Handles text files with proper encoding support.
- **Extensible**: Subclass `FileManager` to add custom file operations.

## Requirements
- Python 3.6+ (uses `abc` module, available in standard library).

No external dependencies.

## Installation
Clone the repository:
   ```bash
   git clone https://github.com/arven338/abstract-file-manager.git
   cd abstract-file-manager
```

## Usage

### Importing the Module
Import the classes from `manager.py`:
```python
from manager import FileReader, FileWriter
```
Reading a file:
```python
reader = FileReader()
content = reader.read_file('example.txt')
print(content)  # Output.
```
Writing a file:
```python
writer = FileWriter()
writer.write_file('example.txt', 'Hello World!')
