from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask! 여진님 최고!'

if __name__ == '__main__':
    app.run(debug=True)
