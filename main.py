from flask import Flask,render_template,request,session,redirect
from db import  Database
import api


app = Flask(__name__)
dbo=Database()
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registraion():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():

    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)


    return render_template('ner.html',response=response)

@app.route('/sentiment')
def sentiment():

    return render_template('sentiment.html')

@app.route('/perform_sentiment',methods=['post'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = api.Sentiment(text)
    txt=''
    for i in response['sentiment']:
        txt = txt + i + ' -> ' + str(response['sentiment'][i]) + '\n'
    print(txt)
    return render_template('sentiment.html', txt=txt)





app.run(debug=True)
