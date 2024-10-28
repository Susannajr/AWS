from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/active')
def active():
    return render_template("active.html")

if __name__ == "__main__":
    app.run(debug=True)