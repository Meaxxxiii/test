from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/how")
def how():
    return render_template("how.html")

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/room-it')
def room_it():
    return render_template('room-it.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

