from flask import Flask, render_template
app = Flask(__name__)

# Flask app with basic template.

# First, go to ex2_template.html and modify it, so
# it prints "hello <name>", where <name> is
# your name, in red.

# Then, use render_template to render
# the ex2_template.html template.
@app.route('/')
def home_page():
    pass

# After doing this, run your code with
# "python exercise2.py" and check out your website!
if __name__ == '__main__':
   app.run(debug = True)