from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
app = Flask(__name__)

def clean_text(sent):
	ps = PorterStemmer()
	swords = stopwords.words('english')
	tokens1 = word_tokenize(sent)
	tokens2 = [x.lower() for x in tokens1 if x.isalpha() or x.isdigit()]
	tokens3 = [x.lower() for x in tokens2 if x not in swords]
	tokens4 = [ps.stem(x) for x in tokens3]
	return tokens4

classifier = joblib.load('classifier.model')
tfidf = joblib.load('preprocessor.model')

@app.route('/')
def student():
	return render_template('spamdetector.html')
	
@app.route('/spamfinder', methods=['GET','POST'])
def result():
	if request.method == 'POST':
		data = dict(request.form)
		message = tfidf.transform([data['message']])
		data['result'] = classifier.predict(message)[0]
		return render_template('spamoutput.html', data=data)

if __name__ == '__main__':
   app.run(debug = True)
