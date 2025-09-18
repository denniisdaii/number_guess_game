from flask import Flask
import random 
app = Flask(__name__)
random_num = random.randint(0,9)


@app.route("/")
def hello():
    return """<h1>Guess a number between 0 and 9</h1>
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"""

@app.route("/<int:number>")
def num_guess(number):
    if number < random_num:
        return """<h1 style='color:red'> Too Low </h1>"""
    if number > random_num:
        return """<h1 style='color:blue'> Too High </h1>"""
    else:
        return """<h1 style='color:green'> You got it! </h1>"""

if __name__ == "__main__":
    app.run(debug=True)