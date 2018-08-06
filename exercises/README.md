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

Add your first HTML template in `templates/index.html`.

Now, use the `render_template` function and 
print your favorite sport as a heading, using a h1 tag.
After this, write a paragraph about why it's clearly the
best sport.

### Part 3: Adding CSS

Add a new rule in `static/style.css` to make all headings in
your website red.

Then, import this file in your HTML template. Open your HTML page
in the browser, to check that your heading is red.

If you have extra time, build a color scheme for your website.

### Part 4: Using Loops and Conditionals!

- First, add a for loop into your template, to print a list
of your favorite players. This list should be defined
inside your Python `home_page` function.

- Use an if-statement, to check if a variable `likes_same_sport`, which
should be defined in your Python file, is True. If it is True,
render the website, as before.

- If it's False, just print the paragraph explaining why you think that it's
the best sport.


### Part 5: Extras

If you finish any of the previous parts early, you can work
on some extra tasks, including:
- Finding and importing more complex templates from W3
- Organize your website using divs
- Add a header to your website, and make sure to use margins and padding
to separate the header from the content on the website
- Adding a sidebar to your website, that doesn't move when you scroll
- Adding images to your website. The list of images should be defined
in the `home_page` function in `app.py`.
- Add a table to the website, with pictures and quotes from the most
memorable players or games. 


