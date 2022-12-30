import json
config = json.load(open("config.json","r"))
class ServerInfo:
    serverBrand = config["brand"]
    exUrl = config["url"]
    digestKey = config["digestKey"]