from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    total_herd = 10
    animals_requiring_attention = 3
    animals_requiring_attention_id = ["Moose","Flanagan","Piper"]
    missing_health_updates = 2
    recent_alerts = 1
    return render_template("dashboard.html", total_herd=total_herd, animals_requiring_attention=animals_requiring_attention, missing_health_updates=missing_health_updates, recent_alerts=recent_alerts, animals_requiring_attention_id=animals_requiring_attention_id)

if __name__ == "__main__":
    app.run(debug=True)