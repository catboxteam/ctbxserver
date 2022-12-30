from flask import Flask
app = Flask(__name__)
import os
import importlib
import json



cfg = {
    'brand':'ctbx',
    'url':'http://127.0.0.1:10060/',
    'digestKey':None
}

if not os.path.exists("r"): os.makedirs("r")
if not os.path.exists("png"): os.makedirs("png")
if not os.path.exists("config.json"):
    open("config.json","w").write(json.dumps(cfg, indent=4))


for root, _, files in os.walk('routes'):
    for file in files:
        if not file.endswith('.py'): continue
        path = os.path.join(root, file[:-3]).replace(os.sep, '.')
        print(f"Imported {path}")
        globals()[file] = importlib.import_module(path)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=10060, debug=True)