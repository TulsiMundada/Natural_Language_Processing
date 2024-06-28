from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
   return ('Hello %s'  %name)
   
@app.route('/')
def hello():
   return ('This is home page')
   
if __name__ == '__main__':
   app.run(debug=True)
