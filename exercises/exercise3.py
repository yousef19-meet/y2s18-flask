from flask import Flask, render_template
app = Flask(__name__)

# Write a function that takes in an input
# variable, num_pets, which defaults to 0 and prints
# "I have <num_pets> pets".
@app.route('/')
def home_page():
	pass

if __name__ == '__main__':
   app.run(debug = True)