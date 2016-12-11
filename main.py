import aiml
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = kernel.respond(text)
    print processed_text
    if processed_text != "":
      return processed_text
    else:
        return "Nan Magand"

if __name__ == '__main__':
    app.debug = True
    app.run()