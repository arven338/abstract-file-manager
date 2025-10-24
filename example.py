# Import
from manager import * # import all functions

# Creating objects
writer = FileWriter()
reader = FileReader()

# Writing example
writer.write_file('example.txt', 'Hello World!')

# Reading example
content = reader.read_file('example.txt')
print(content)
