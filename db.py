import psycopg


conn = psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=postgres")
conn.commit()

def insert_person(person):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO persons (person_id, name, sex, colony, age) VALUES (%s, %s, %s, %s, %s)",
        (person.id, person.name, person.sex, person.colony, person.age))
    conn.commit()

def remove_person(person):
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM orders WHERE person_id = person_id")
    conn.commit()

