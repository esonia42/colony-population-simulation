import psycopg
from psycopg_pool import ConnectionPool


class DbInterface:
    def __init__(self):
        self.single_conn = self.get_conn()
        self.pool = self.get_pool()

    def get_pool(self):
        pool = ConnectionPool("host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10 sslmode=prefer")
        return pool

    def get_conn(self):
        conn = psycopg.connect("host=localhost port=5432 dbname=postgres user=postgres password=postgres connect_timeout=10 sslmode=prefer")
        conn.commit()
        return conn

    def insert_persons(self, person):
        cur = self.single_conn.cursor()
        cur.execute(
            "INSERT INTO persons (person_id, sex, age, name, colony) VALUES (%s, %s, %s, %s, %s)",
            (person.id, person.sex, person.age, person.name, person.colony.name))
        self.single_conn.commit()

    def remove_persons(self, person):
        cur = self.single_conn.cursor()
        cur.execute(
            "DELETE FROM persons WHERE person_id = %s", (person.id, ))
        self.single_conn.commit()

    def get_persons(self):
        cur = self.single_conn.cursor()
        cur.execute("SELECT * FROM persons;")
        cur.fetchall()
        self.single_conn.commit()

    def delete(self):
        cur = self.single_conn.cursor()
        cur.execute("DELETE FROM persons;")
        cur.fetchall()
        self.single_conn.commit()

    def get_one_person(self):
        with self.pool.connection() as conn:
            return conn.execute("SELECT * FROM persons;").fetchone()

    def get_multiple_persons(self, n):
        with self.pool.connection() as conn:
            return conn.execute("SELECT * FROM persons;").fetchmany(n)

    def loop_over_tasks(self, number_of_tasks: int):
        for i in range(number_of_tasks):
            self.get_one_person()
        print(number_of_tasks, " finished")

    def close_pool(self):
        self.pool.close()

#class MegaDbInterface(DbInterface):
#    def extra_function(self):
#        pass

#megadb = MegaDbInterface()
#megadb.get_multiple_persons()