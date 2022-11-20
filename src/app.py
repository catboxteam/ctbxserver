from flask import Flask
app = Flask(__name__)
import os
import importlib


for root, _, files in os.walk('routes'):
    for file in files:
        if not file.endswith('.py'): continue
        path = os.path.join(root, file[:-3]).replace(os.sep, '.')
        print(f"Imported {path}")
        globals()[file] = importlib.import_module(path)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=10060, debug=True)