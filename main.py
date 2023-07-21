import pymysql
import dotenv
import os

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DB"],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS songs ("
            "id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, "
            "name VARCHAR(20), "
            "album VARCHAR(20)"
            ")"
        )
