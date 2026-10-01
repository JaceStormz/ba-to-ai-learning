""" import sys
import requests

print("Python:", sys.version.split()[0])
print("requests:", requests.__version__)
print("Hello from inside the venv!") """

class Planet:
    def __eq__(self, other):
        if not isinstance(other, Planet):
            return NotImplemented
        
        
        return self.name == other.name

