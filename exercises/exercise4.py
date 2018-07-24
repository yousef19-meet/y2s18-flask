from flask import Flask, render_template
app = Flask(__name__)

# Write a function, which creates a Boolean
# variable likes_dessert, and a list of
# strings favorite_desserts. Pass these in
# to the appropriate function to be rendered in HTML.
@app.route('/')
def home_page():
	pass

if __name__ == '__main__':
   app.run(debug = True)