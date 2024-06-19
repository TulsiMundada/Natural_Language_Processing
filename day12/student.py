from flask import Flask , render_template , request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('readmarks.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
      if request.method == 'POST':
            phy = int(request.form['phy'])
            che = int(request.form['che'])
            mat = int(request.form['mat'])
            avg = (phy+che+mat)/3
            return render_template("result.html", result = avg)

if __name__ == "__main__":
        app.run(debug=True)