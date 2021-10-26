import os
import subprocess
import ast

path = os.path.dirname(os.path.realpath(__file__))

with open("data.txt", "r") as file:
    contents = file.read()
    data = ast.literal_eval(contents)
i = 1
for url in data.keys():
    subprocess.Popen(f'python {path}/bot.py "{url}" "{data[url]}" "{i}"')
    i += 1
