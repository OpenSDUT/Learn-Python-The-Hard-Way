# study drill 2
from sys import argv

script, filename = argv

with open(filename) as txt:
    print txt.read()
