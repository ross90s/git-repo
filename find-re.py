#! python
import sys
import re
f = open("text-file", "r")
print(f.read())
#Comment
m = f.read()
x = re.search("MB", m)
print x.string[x.start():x.end()]