from flask import Flask, render_template
app = Flask(__name__)

# PART 1: Write a function, using just Python, to display your
# name on the home page, when you run the website

# PART 2: Write a basic HTML template to add a
# secondary heading underneath your name to include
# your year and favorite candy.

# PART 3: Use CSS attributes (Hint: look at the other templates
# we provided as examples) to make the background of your website
# your favorite color and the text white!

# PART 4: Make your website prettier - this can include
# finding more complex templates online, or adding some more CSS
# tricks of your own!

if __name__ == '__main__':
   app.run(debug = True)