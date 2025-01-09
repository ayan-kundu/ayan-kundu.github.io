from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_comment', methods=['POST'])
def send_comment():
    comment = request.form['comment_box']
    msg = Message('New Comment from Harvey House Group Chat',
                  sender='your-email@gmail.com',
                  recipients=['Ayanwes@gmail.com'])
    msg.body = f'New comment: {comment}'
    mail.send(msg)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
