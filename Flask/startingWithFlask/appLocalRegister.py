from flask import Flask, render_template,request
import datetime
import os



app = Flask(__name__)

# routing index and submit templates
@app.route('/') #decorators like @app.route are used to bind a function to a specific URL
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    user_input_dir_name = "User Inputs"
    comment_file_name=os.path.join(user_input_dir_name,'User comments.txt')
    
    # Get the text input from the form
    userInput = request.form.get('user_input') 
    #userInput = 'FUCK YOU!'
    currentTime=datetime.datetime.now().strftime("%m-%d %H:%M")

    # write the user input to database
    comment_to_file(userInput,comment_file_name)
    # return submit template to lauch submit page 
    return render_template('submit.html',user_input=userInput,current_time=currentTime)

# write the user input onto a text file in parent dir 
def comment_to_file(userInput,file_name):
    content = f"{datetime.datetime.now().strftime("%m-%d %H:%M")} -> User Input: {userInput}\n"
    with open (file_name,'a') as f:
        f.write(content)
    print('A comment is written in database!')


if __name__ == '__main__':
    user_input_dir_name = "User Inputs"
    comment_file_name=os.path.join(user_input_dir_name,'User comments.txt')
    if not os.path.exists(user_input_dir_name):
        os.makedirs(user_input_dir_name, exist_ok=True) 
        with open (comment_file_name,'a') as file:
            file.write(f"File created: {datetime.datetime.now().strftime("20%y-%m-%d %H:%M")}\n")
            file.write("\t\t-----------------------------\n")
        print("Dir {user_input_dir_name} to save user input has been created")
    app.run(debug=True)
