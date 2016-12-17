
import re

file_path = r"/Users/floyda/SublimeVideo/example/channel_v3.json"

with open(file_path, "r") as fp:
    content = fp.read()
    fp.close()

result = ""
pattern = "\"name\""

while True:
    pos = content.find(pattern)
    print pos
    if pos < 0 :
        break
    result += content[:pos] + "\n"
    result += pattern
    content = content[pos + len(pattern):]


with open(file_path, "w") as fp:
    fp.write(result)
    fp.close()
