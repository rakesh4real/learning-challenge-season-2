from flask import Flask
app = Flask(__name__)

# Both urls below will return same funtion home()
@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

# Note: Function's name same as url
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# True when script is run directly using python
if __name__ == '__main__':
    app.run(debug=True)
