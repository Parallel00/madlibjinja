from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def question():
    prompt = story.prompts
    
    return render_template("question.html", prompt=prompt)
    
@app.route("/story")
def stryshw():
    text = story.generate(request.args)
    return render_template("story.html", text=text)