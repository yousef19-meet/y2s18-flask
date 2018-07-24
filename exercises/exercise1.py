from flask import Flask, render_template
app = Flask(__name__)

# Fill in the function home_page to print
# "Hello <name>" where <name> is your name!
@app.route('/')
def home_page():
    pass

# Run your website by running
# "python first_app.py"
if __name__ == '__main__':
   app.run(debug = True)