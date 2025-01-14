from flask import Flask, render_template,request
import datetime

app = Flask(__name__)

@app.route('/') #decorators like @app.route are used to bind a function to a specific URL
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    # Get the text input from the form
    userInput = request.form.get('user_input') 
    #userInput = 'FUCK YOU!'
    currentTime=datetime.datetime.now().strftime("%m-%d %H:%M")
    return render_template('submit.html',user_input=userInput,current_time=currentTime)

if __name__ == '__main__':
    app.run(debug=True)


