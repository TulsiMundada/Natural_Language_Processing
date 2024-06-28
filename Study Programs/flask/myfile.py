from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_admin():
   return 'Welcome to Tushar\'s Computer! '

if __name__ == '__main__':
   app.run(host='192.168.76.169', debug = True)
