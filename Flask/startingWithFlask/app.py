from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    # Get the text input from the form
    #userInput = request.form.get('user_input') 
    userInput = 'FUCK YOU!'
    return render_template('submit.html',user_input=userInput)

if __name__ == '__main__':
    app.run(debug=True)
