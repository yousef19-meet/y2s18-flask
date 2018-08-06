### Y2 2018 Summer: Basic Flask Lab

Welcome to the Intro to Flask lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

Throughout this lab, you should be editing `app.py`.

### Part 1: First web page!

Edit the `home_page` function, using just Python, to print your favorite sport.
A stub for this function can be found in app.py.

Make sure you run `python app.py` to see your favorite sport
printed in your browser.

### Part 2: Adding a Template!

Add your first HTML template inside the `templates` directory.

Now, use the `render_template` function and 
print your favorite sport as a heading, using a h1 tag.
After this, write a paragraph about why it's clearly the
best sport.

### Part 3: Adding CSS

Create a new file `style.css` in the directory.
Do you remember where this file goes?

Import this file in your HTML template and use it to make
the heading of your website red. If you have extra time, build a color scheme
for your website.

### Part 4: Using Loops and Conditionals!

- Now, add a for loop into your template, to print a list
of your favorite players. This list should be defined
inside your Python `home_page` function.

- Use an if-statement, to check if a variable `likes_same_sport`, which
should be defined in your Python file, is True. If it is True,
render the website, as before.

- If it's False, just print the paragraph explaining why you think that it's
the best sport.


### PART 5: Extras

Make your website prettier - this can include
finding more complex templates online, or adding some more CSS
tricks of your own!
