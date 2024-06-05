# Espresso Haven

Espresso Haven is a coffee shop website that allows users to register, log in, view menu items, read reviews, and leave feedback. The website is built using Flask, SQLite, and Flask-Mail for email functionality.

## Features

- User Registration and Login
- View Coffee Menu
- Submit Reviews and Feedback
- Display User Reviews
- Send Discount Email upon Registration
- Privacy Policy Page

## Technologies Used

- Flask
- SQLite
- Flask-Mail
- HTML/CSS
- JavaScript

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/espresso-haven.git
   cd espresso-haven


## Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the required packages:
- pip install -r requirements.txt

## Set up environment variables:
- Create a .env file in the root directory and add the following:
- SECRET_KEY=your_secret_key
- MAIL_USERNAME=your_email@example.com
- MAIL_PASSWORD=your_email_password
- FLASK_DEBUG=True

## Initialize the database:
>>> python
>>> from app import init_db
>>> init_db()
>>> exit()


## Run the application:
- flask run


## Project Structure:

espresso-haven/
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── style_login.css
│   │   └── style_register.css
│   ├── images/
│   │   └── (all images used in the website)
│   └── svg/
│       └── (all SVG icons used in the website)
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── policy.html
│   └── register.html
│
├── .env
├── app.py
├── requirements.txt
└── README.md


## Usage:

- Home Page
- Displays the coffee shop's menu and user reviews.
- Users can navigate to the login, register, or policy pages.
- User Registration
- Users can register by providing a username, email, and password.
- Upon successful registration, a discount email is sent to the user's email address.
- User Login
- Registered users can log in by providing their username and password.
- Upon successful login, users are redirected to the home page.
- Reviews and Feedback
- Users can submit reviews and feedback through the home page.
- All reviews are displayed on the home page.
- Privacy Policy
- The privacy policy page outlines how user information is collected, used, and protected.
- License
- This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements:

- Flask
- SQLite
- Flask-Mail

Enjoy your coffee experience with Espresso Haven! ☕





