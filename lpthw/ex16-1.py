# This program is for read the file we created in ex16.py 
from sys import argv

script, filename = argv

print(f"Hi, I'm {script} script and I will read {filename} file.")

txt = open(filename)
content = txt.read()

print(f"\n{content}")
content.close()