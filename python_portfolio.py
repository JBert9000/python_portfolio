from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "This is the Homepage"

@app.route('/about/')
def about():
    return "The about content goes here...."

if __name__=="__main__":
    app.run(debug=True)