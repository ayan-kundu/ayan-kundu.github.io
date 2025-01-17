from flask import Flask, render_template,request
import datetime
import smtplib

app = Flask(__name__)

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
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "ayanwesha@gmail.com"
    sender_password = "Ayanwesha1010" 
    receiver_email = "ayanwesha@gmail.com"

    subject = "User Input from Flask App"
    body = f"User Input: {userInput} @ {currentTime}"
    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email using SSL
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)





if __name__ == '__main__':
    app.run(debug=True)


