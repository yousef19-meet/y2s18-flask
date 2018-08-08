from flask import Flask, render_template
app = Flask(__name__)
#part 1
@app.route('/')
def home_page():
    # x= "get off my lawn bish... but /sport and get outta here"
    # print(x)
    songs=["home-passenger", "let her go- passenger", "bohemian rapsody- queen"]
    return render_template(
    "index.html",
    songs=songs,
    likes_same_singer=True)

    
#############
#part 2
@app.route('/sport') 
def favorite_sport():
    return render_template ("index.html")
#############
#part 3
@app.route('/green')
def hello_world():
    return render_template(
"index.html")
#############
#part 






#############
if __name__ == '__main__':
   app.run(debug = True)