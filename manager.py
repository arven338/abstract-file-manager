# Imports
from abc import ABC, abstractmethod

# Abstract class
class FileManager(ABC):
    @abstractmethod
    def explore(self, path, *args, **kwargs):
        pass

# Reader class
class FileReader(FileManager):
    def read_file(self, path):
        return self.explore(path)
        
    def explore(self, path, *args, **kwargs):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

# Writer class
class FileWriter(FileManager):
    def write_file(self, path, msg, mode='w'):
        self.explore(path, msg, mode)
        
    def explore(self, path, msg, mode='w', *args, **kwargs):
        with open(path, mode, encoding='utf-8') as file:
            file.write(msg)
