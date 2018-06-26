from flask import Flask , render_template
app = Flask(__name__)

posts = [
    {
     'author':'Maxwell Haron',
     'title':'Blog Post 1',
     'content':'First post content',
     'date_posted':'April 20, 2018'
    },
    {
      'author':'Catherine Pierce ',
      'title':'Blog Post 2',
      'content':'Second post content',
      'date_posted':'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/About")
def about():
    return render_template('about.html' , title = about)

if __name__ == '__main__':
    app.run(debug=True)
