from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

'''
def show_elements():
	return "Ayän! Welcome to Flask and webApp"
'''


if __name__ == '__main__':
	app.run(debug=True)
	