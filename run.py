from flask import Flask
import random
littale = "qwertyuiopasdfghjklzxcvbnm"
email = "".join(random.choice(littale) for _ in range(6))
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello "+ email



app.run(debug=True)