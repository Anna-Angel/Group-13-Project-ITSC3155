from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "my_secret_key"  # Set a secret key for session management

# User Data to Login
USERS = [
    {"username": "Ishan", "password": "Ishan101"},
    {"username": "Sharma", "password": "Sharma101"}
]

# Global Discussion Board (temporary storage for messages)
DISCUSSION_BOARD = []

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
                # If login is successful, store the username in the session
                session['username'] = username
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

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if 'username' not in session:
        return redirect('/login') 

    if request.method == 'POST':
        # Get the message from the form
        message = request.form['message']
        # Get the username from the session
        username = session['username']

        # Create a new message with username and message content
        new_message = {"username": username, "message": message}
        # Add the new message to the global discussion board
        DISCUSSION_BOARD.append(new_message)

    return render_template('welcome.html', messages=DISCUSSION_BOARD, username=session['username'])

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect('/login')

    return render_template('profile.html', username=session['username'])

@app.route('/change', methods=['GET', 'POST'])
def change():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        # Get username and ask user for new password
        username = session['username']
        password = request.form.get('password')

        #update password in dictionary
        x = 0
        while x in range(len(USERS)):
            if USERS[x]['username'] == username:
                USERS[x]['password'] = password
                break

    return render_template('change.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)
