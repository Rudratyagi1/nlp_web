from db import Database
from flask import Flask, render_template, request, jsonify, redirect
from api import ner, sentiment_analysis, abuse_detection

app = Flask(__name__)
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=["POST"])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_pass')
    response = dbo.insert(name, email, password)

    if response == 1:
        return render_template('login.html', message='Registration success. Login now.')
    else:
        return render_template('register.html', message='Email already exists.')

@app.route('/perform_login', methods=["POST"])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    response = dbo.search(email, password)

    if response == 1:
        return redirect('/profile')  # Login successful
    else:
        return render_template('login.html', message='Invalid email or password. Please try again.')

@app.route('/profile')
def profile():
    return render_template('profile.html')  # Ensure you have a profile.html template

@app.route('/ner')
def ner_1():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    entities = ner(text)
    return jsonify({"entities": entities})

@app.route('/perform_sentiment_analysis', methods=['POST'])
def perform_sentiment_analysis():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    sentiment = sentiment_analysis(text)
    return jsonify({"sentiment": sentiment})

@app.route('/perform_abuse_detection', methods=['POST'])
def perform_abuse_detection():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    abuse_result = abuse_detection(text)
    return jsonify({"abuse_detected": abuse_result})

if __name__ == '__main__':
    app.run(debug=True)
