from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, auth, firestore
app = Flask(__name__)

cred = credentials.Certificate("firebase_key.json")  
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        action = request.form['action']  
        email = request.form['email']
        password = request.form['password']

        if action == 'signup':
            username = request.form['username']
            try:
                user = auth.create_user(
                    email=email,
                    password=password
                )
                db.collection('users').document(user.uid).set({
                    'username': username,
                    'email': email
                })
                message = "Signup successful! You are logged in!"
            except Exception as e:
                message = f"Signup Error: {str(e)}"

        elif action == 'login':
            try:
                # Try to fetch user by email
                user = auth.get_user_by_email(email)
                message = "Login successful! You are logged in!"
            except Exception as e:
                message = f"Login Error: Invalid credentials or {str(e)}"

    return render_template('home.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
