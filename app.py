import os
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for the Flask application
app.secret_key = os.environ.get('SECRET_KEY', '429d56ce8188afb4ce934c3c5c9394ca')

# Configure Flask-Mail for email sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

# Initialize the Mail object with the Flask app configuration
mail = Mail(app)

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to initialize the database with required tables
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            email TEXT NOT NULL,
            rating TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route for the home page
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    conn.close()
    return render_template('index.html', reviews=reviews)

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           (username, email, hashed_password))
            conn.commit()
            # Send the discount email
            if send_discount_email(email):
                flash('Registration successful! Please check your email for the discount code.')
            else:
                flash('Registration successful, but we could not send the discount email.')
            return redirect(url_for('home', registered='true'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists.')
        finally:
            conn.close()

    return render_template('register.html')

# Function to send a discount email to the user
def send_discount_email(to_email):
    try:
        msg = Message('Your 5% Discount Code', recipients=[to_email])
        msg.body = 'Thank you for registering with Espresso Haven! Use the code COFFEE5 to enjoy a 5% discount on your next purchase.'
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            flash('Login successful!')
            return redirect(url_for('home'))  
        else:
            flash('Invalid username or password.')
        conn.close()

    return render_template('login.html')

# Route for the privacy policy page
@app.route('/policy')
def policy():
    return render_template('policy.html')

# Main entry point of the application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')
