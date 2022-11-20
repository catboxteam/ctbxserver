from routes import *
from flask import Flask

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':

    app.run(debug=True,port=10060)