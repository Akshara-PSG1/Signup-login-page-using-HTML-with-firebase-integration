This is a simple implementation of sign up/ login system with Firebase integration.
Note: This repository doesn't consist firebase_key.json file for security concerns.

Procedure:
1. Go to https://console.firebase.google.com/ . Click "Add Project" and give the project a name (e.g., user-login-creds)
2. Enable Authentication: In Firebase Console, left sidebar ➔ Go to Authentication ➔ Get Started. In Sign-in methods, enable Email/Password authentication.
3. Set up Firestore Database: In Firebase Console, left sidebar ➔ Go to Firestore Database.
Click "Create database" , Choose Start in test mode (for development) and then Click Enable.
4. Get Service Account Key (firebase_key.json): In Firebase Console, ➔Project Settings→ Service Accounts. Click Generate new private key and It downloads a JSON file and saves it as firebase_key.json in the project folder.
5. Run app.py. It runs on localhost. When the user signs up, the credentials are stored in the firebase filestore. Now the user can login next time, since authentication is done.          
Login fails with an error if no user account exists.
When the same user signs up for the 2nd time, it gives an error.

View the FireStore Database, to see the users who have an account. 
This can be integrated with some other projects that require a sign up/ login Page with Authentication. 
