from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my first Python app deployed from GitHub 🚀"

@app.route("/about")
def about():
    return "Built by a learner who is leveling up step by step 😄"

if __name__ == "__main__":
    app.run(debug=True)
