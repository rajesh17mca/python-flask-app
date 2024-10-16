from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is / URI and called as root!'

if __name__ == '__main__':
    app.run()

