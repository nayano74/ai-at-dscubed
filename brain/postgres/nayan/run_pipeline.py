import psycopg2
from pathlib import Path

# Update this with the actual RDS endpoint
DB_ENDPOINT = "darcydb.crgk48smefvn.ap-southeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "7crQ9MrrBC216QmgSB^S"
DB_PORT = 5432

def get_connection():
    return psycopg2.connect(
        host=DB_ENDPOINT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

def run_sql_script(script_path: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = Path(script_path).read_text()
            cur.execute(sql)
            conn.commit()
            print(f"Executed script: {script_path}")

def view_table(schema: str, table: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {schema}.{table} LIMIT 10;")
            rows = cur.fetchall()
            for row in rows:
                print(row)

if __name__ == "__main__":
    # Adjust name as needed
    run_sql_script("brain/postgres/nayan/DDL/create_nayan.sql")
    run_sql_script("brain/postgres/nayan/DML/insert_nayan.sql")
    view_table("project_two", "nayan")
