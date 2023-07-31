from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# User Data to Login
USERS = [
    {"username": "Ishan", "password": "Ishan101"},
    {"username": "Sharma", "password": "Sharma101"}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check DB for existing username and matching password
        for user in USERS:
            if user['username'] == username and user['password'] == password:
                # If login is successful, redirect to the welcome page
                return redirect('/welcome')

        # If login fails, reload the dashboard page
        return redirect('/')

    # If the request method is GET, render the login form
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        for user in USERS:
            if user['username'] == username:
                return "Username already exists. Please choose a different username."

        # If the username is unique, add the new user to the database
        USERS.append({"username": username, "password": password})

        # Redirect the user to the login page after successful signup
        return redirect('/')

    # If the request method is GET, render the signup form
    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    return "Welcome! You have successfully logged in."

if __name__ == '__main__':
    app.run(debug=True)
