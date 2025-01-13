import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    USER_INPUT = request.form.get('user_input')  # Get the text input from the form
    send_email(USER_INPUT)  # Send the email
    return render_template('submit.html', user_input=USER_INPUT)

def send_email(user_input):
    # Email configuration
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "ayan@gmail.com"
    sender_password = "your_email_password"  # Use your Gmail password or an app-specific password
    receiver_email = "ayan@gmail.com"
    subject = "User Input from Flask App"
    body = f"User Input: {user_input}"

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email using SSL
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    app.run(debug=True)
