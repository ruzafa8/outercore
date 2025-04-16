import pandas
import psycopg2

class PostgresConnection:
    def __init__(self, config):
        self.config = {
                "host": config.get("host", "localhost"),
                "port": config.get("port", "5432"),
                "database": config.get("database", "default"),
                "user": config.get("user", "postgres"),
                "password": config.get("password", "postgres"),
        }
        self.connection = None

    def __enter__(self):
        try:
            with psycopg2.connect(**self.config) as conn:
                self.connection = conn
                print("Connetion sucessfully")
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            self.connection = None

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.connection:
            self.connection.close()

def load_csv(filename):
    return pandas.read_csv(filename)

def main():
    db_config = {"database": "piscineds", "user": "aruzafa-", "password": "mysecretpassword"}
    with PostgresConnection(db_config) as db:
        pass
    # r = load_csv("data_2022_dec.csv")
    # print(r)

if __name__ == "_main_":
    main()