from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

if __name__ == "__main__":
    # debug=True permite ver erros detalhados e auto-reload
    app.run(debug=True)