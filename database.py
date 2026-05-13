import sqlite3
from datetime import datetime

#Get time
def get_time():
    time = datetime.now()
    date = time.strftime("%m/%d/%Y")

    return date


def database_connect():
    conn = sqlite3.connect("data.db", timeout=10) #Connects to the database file
    conn.row_factory = sqlite3.Row #Allows access the rows by the name (e.g: line["name"]) instead of the index (e.g: line[0])
    conn.execute("PRAGMA foreign_keys = ON")
    return conn



def initialize_database():
    conn = database_connect()


    #ANIMAL TABLE
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cattle (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- ID of the animal,
            arrival_day DATE, -- day which the animal came to the ranch
            tag TEXT UNIQUE, -- physical identification of the animal
            race TEXT, -- Race, ex: Angus, Nelore
            sex TEXT CHECK(sex IN('M', 'F')), -- Only M(for males) or F(for females)
            birth_day DATE,
            status TEXT DEFAULT 'Active' -- Active, Sold or Dead
            )
                 
                 
        """)
    
    #WEIGHT TABLE
    conn.execute("""
            CREATE TABLE IF NOT EXISTS weights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cattle_id INTEGER NOT NULL,
            weight REAL,
            weigh_day DATE NOT NULL,

            FOREIGN KEY (cattle_id) -- Connection with the cattle table
            REFERENCES cattle(id) -- Look at the id column inside the cattle table
            ON DELETE CASCADE -- When delete the animal from table cattle, also deletes its weight here
            )
                 """)

    conn.commit()
    conn.close()


#CREATE INFO

def new_animal(tag, arrival_day, race, sex, birth_day, weight):
    conn = database_connect()
    try:
        #Insert animal
        cursor = conn.execute("""
                INSERT INTO cattle (tag, arrival_day ,race, sex, birth_day) 
                VALUES (?, ?, ?, ?, ?)
            """, (tag, arrival_day, race, sex, birth_day))
        
        #Get generated animal id
        cattle_id = cursor.lastrowid


        #Insert initial weight
        conn.execute("""
                INSERT INTO weights (cattle_id, weight, weigh_day)
                VALUES (?, ?, ?)
                """, (cattle_id, weight, get_time()))


        conn.commit()  # Salva as alterações
    except Exception as e:
        print(f"Error when adding: {e}")
    finally:
         conn.close()


def delete_animal(cattle_id):
    conn = database_connect()
    try:
        conn.execute("DELETE FROM cattle WHERE id = ?", (cattle_id,))
        conn.commit()
    finally:
        conn.close()


def add_weight(cattle_id, new_weight):
    conn = database_connect()
    try:
        #Get last weight
        last = conn.execute("""
            SELECT weight
            FROM weights
            WHERE cattle_id = ?
            ORDER BY id DESC
            LIMIT 1
        """, (cattle_id,)).fetchone()

        if last:
            old_weight = last["weight"] #-> Defines the old weight
            difference = new_weight - old_weight #-> Set the difference between actual and last weight
            print(f"Difference: {difference} kg")


        #Inserting the new values into weights table
        conn.execute("""
            INSERT INTO weights (
            cattle_id,
            weight,
            weigh_day
            )
            VALUES (?, ?, ?)
        """, (
            cattle_id,
            new_weight,
            get_time()
        ))

        conn.commit()
        
    except Exception as e:
        print(f"Error when adding: {e}")
    finally:
        conn.close()


def search_all():
    conn = database_connect()
    data = conn.execute("SELECT * FROM cattle").fetchall()
    conn.close()
    return data




### GET INFO
def get_animal_count():
    conn = database_connect()
    data = conn.execute("SELECT COUNT(*) FROM cattle")
    count = data.fetchone()[0]
    conn.close()

    return count    