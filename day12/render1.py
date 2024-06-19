from flask import Flask , request , redirect , url_for
app = Flask(__name__)

@app.route('/')
def index():
    return '''<html><body>
                <h1>Hello Deepika</h1>
                Your love is waiting at
                @ CDAC, Pune
              </body></html>'''

if __name__ == "__main__":
        app.run(debug=True)