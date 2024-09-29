from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to store session data

# Helper function to initialize session
def initialize_session():
    if 'jackpot' not in session:
        session['jackpot'] = random.randint(1, 100)
    if 'counter' not in session:
        session['counter'] = 0

# Route for the home page
@app.route('/')
def index():
    initialize_session()  # Initialize session variables if not present
    return render_template('index.html')

# Route for processing the guess
@app.route('/guess', methods=['POST'])
def guess():
    initialize_session()  # Ensure session variables are initialized
    guess = request.form.get('guess')
    if guess:
        try:
            guess = int(guess)
            session['counter'] += 1  # Increment counter
            jackpot = session['jackpot']
            
            if guess < jackpot:
                message = "Guess higher!"
            elif guess > jackpot:
                message = "Guess lower!"
            else:
                message = f"Congratulations! You guessed it in {session['counter']} attempts."
                session.pop('jackpot', None)  # Clear the jackpot to start a new game
                session.pop('counter', None)
            return render_template('index.html', message=message)
        except ValueError:
            message = "Please enter a valid number!"
            return render_template('index.html', message=message)
    return redirect(url_for('index'))

# Route to reset the game
@app.route('/reset')
def reset():
    session.pop('jackpot', None)  # Remove the jackpot from session to start a new game
    session.pop('counter', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
