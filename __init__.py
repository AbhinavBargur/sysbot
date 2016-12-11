from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template("ui1.html")



if __name__ == "__ui1__":
  app.run()