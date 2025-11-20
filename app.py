from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/how")
def how():
    return render_template("how.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    # ใช้ port 5000 หรือ port อื่นที่คุณต้องการ เช่น 5500