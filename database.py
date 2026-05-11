import sqlite3

def database_connect():
    conn = sqlite3.connect("data.db", timeout=10) #Connects to the database file
    conn.row_factory = sqlite3.Row #Allows access the rows by the name (e.g: line["name"]) instead of the index (e.g: line[0])
    return conn



def initialize_database():
    conn = database_connect()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cattle (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- ID of the animal,
            tag TEXT UNIQUE, -- physical identification of the animal
            race TEXT, -- Race, ex: Angus, Nelore
            sex TEXT CHECK(sex IN('M', 'F')), -- Only M(for males) or F(for females)
            birth_day DATE,
            weight REAL, -- Weight for future analysis
            status TEXT DEFAULT 'Active' -- Active, Sold or Dead
            )
                 
                 
        """)
    conn.commit()
    conn.close()

def new_animal(tag, race, sex, birth_day, weight):
    conn = database_connect()
    try:
        conn.execute("""
                INSERT INTO cattle (tag, race, sex, birth_day, weight) 
                VALUES (?, ?, ?, ?, ?)
            """, (tag, race, sex, birth_day, weight))
        conn.commit()  # Salva as alterações
    except Exception as e:
        print(f"Erro ao inserir: {e}")
    finally:
         conn.close()


def delete_animal(animal_id):
    conn = database_connect()
    try:
        conn.execute("DELETE FROM cattle WHERE id = ?", (animal_id,))
        conn.commit()
    finally:
        conn.close()

def search_all():
    conn = database_connect()
    data = conn.execute("SELECT * FROM cattle").fetchall()
    conn.close()
    return data