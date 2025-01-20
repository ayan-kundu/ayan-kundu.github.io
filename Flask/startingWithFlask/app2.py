from flask import Flask, render_template,request
import datetime

# for sending through mail
import smtplib
from flask_mail import Mail, Message
# for writing onto one drive 
import onedrivesdk 


app = Flask(__name__)

# Configure Flask-Mail 
app.config['MAIL_SERVER'] = 'smtp.gmx.com' 
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USERNAME'] = 'Ayana@gmx.co.uk' 
app.config['MAIL_PASSWORD'] = 'Ayanwesha1010' 
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True 
mail= Mail(app)


# routing index and submit templates
@app.route('/') #decorators like @app.route are used to bind a function to a specific URL
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    # Get the text input from the form
    userInput = request.form.get('user_input') 
    #userInput = 'FUCK YOU!'
    currentTime=datetime.datetime.now().strftime("%m-%d %H:%M")

    # send the user input to admin mail
    send_email(userInput, currentTime)
    # return submit template to lauch submit page 
    return render_template('submit.html',user_input=userInput,current_time=currentTime)

# routing user input given to index 
def send_email(userInput,currentTime):
    sender_email = "Ayana@gmx.co.uk"
    sender_password = "Ayanwesha1010" 
    receiver_email = "Ayana@gmx.co.uk"

    # for Flask Mail
    subject = "User Input from Flask App" 
    body = f"User Input: {userInput} @ {currentTime}"
    msg = Message(subject, sender=sender_email, recipients=[receiver_email]) 
    msg.body = body 
    with app.app_context(): 
        mail.send(msg)

    # for smtp
    # smtp_server = "mail.gmx.com"
    # port = 465
    # # Send the email using SSL
    # with smtplib.SMTP_SSL(smtp_server, port) as server:
    #     server.login(sender_email, sender_password)
    #     server.sendmail(sender_email, receiver_email, message)



if __name__ == '__main__':
    app.run(debug=True)
