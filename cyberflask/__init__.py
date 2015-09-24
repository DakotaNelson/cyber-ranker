from flask import Flask

app = Flask(__name__)
app.debug = False

if __name__ == '__main__':
    app.run()
