from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('read_in.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      phy = int(request.form['phy'])
      che = int(request.form['che'])
      mat = int(request.form['mat'])
      avg = (phy+che+mat)/3
      if avg >= 75:
      	result="Distinction"
      elif avg >= 60:
      	result="First Class"
      elif avg >= 50:
      	result = "Second Class"
      elif avg >= 40:
      	result = "Pass Class"
      else:
      	result = "FAILED!"
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(host="192.168.76.169", debug = True)
   
   
