from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

database.initialize_database() #Creates the database right when the app starts

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    total_herd = database.get_animal_count()
    animals_requiring_attention = 3
    animals_requiring_attention_id = ["Moose","Flanagan","Piper"]
    missing_health_updates = 2
    recent_alerts = 1
    return render_template("dashboard.html", total_herd=total_herd, animals_requiring_attention=animals_requiring_attention, missing_health_updates=missing_health_updates, recent_alerts=recent_alerts, animals_requiring_attention_id=animals_requiring_attention_id)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        tag = request.form.get("input_tag")
        race = request.form.get("input_race")
        sex = request.form.get("input_sex")
        birth_day = request.form.get("input_birthday")
        weight = request.form.get("input_weight")

        print(f"DEBUG -> Tag: {tag}, Raça: {race}")
        database.new_animal(tag, race, sex, birth_day, weight)
        return redirect("/animals")
    
    return render_template("register.html")

@app.route("/animals")
def animals():
    all_animals = database.search_all()
    return render_template("animals.html", animals_list=all_animals)

@app.route("/delete", methods=["POST"])
def delete():
    delete_id = request.form.get("animal_id")
    if delete_id:
        database.delete_animal(int(delete_id)) # SQLite can't receive an string. To make sure I convert everytime here.
    return redirect("/animals")

if __name__ == "__main__":
    app.run(debug=True)