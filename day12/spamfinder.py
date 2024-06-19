import joblib
#import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from flask import Flask , render_template , request

def clean_text(sent):
    swords = stopwords.words('english')
    ps =  PorterStemmer()
    tokens1 = word_tokenize(sent)
    token2 = [token for token in tokens1 if token.isalnum()]
    tokens3 = [token for token in token2 if token.lower() not in swords]
    tokens4 = [ps.stem(x) for x in tokens3]
    return tokens4

classifier = joblib.load('C:/Users\\dai\\Desktop\\NLP\\daywise_lab\\day12\\classifier.model')
tfidf = joblib.load('C:/Users\\dai\\Desktop\\NLP\\daywise_lab\\day12\\preprocessor.model')

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('spamdetector.html')

@app.route('/spamfinder',methods = ['POST', 'GET'])
def result():
      if request.method == 'POST':
            data = dict(request.form)
            message = tfidf.transform([data['message']])
            data['result'] = classifier.predict(message)[0]
            return render_template('spamoutput.html' , data = data)
            
if __name__ == "__main__":
        app.run(debug=True)