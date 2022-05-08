import logging
import psycopg2
from config import host, user, db_name, password

logging.basicConfig(level=logging.WARNING, filename='logfile.txt')


try:
    connect = psycopg2.connect(database=db_name, password=password, user=user, host=host)
    connect.autocommit = True

except Exception:
    logging.critical('Нет подключения к бд')

UniqueViolation = psycopg2.errors.lookup('23505')


def insert_post(js):
    if connect:
        with connect.cursor() as cur:
            try:
                cur.execute(
                    f"insert into questions(id, question, answer, created) values({js['id']}, '{js['question']}', '{js['answer']}', '{js['created_at']}')")
                return 1
            except UniqueViolation:
                return 0
            except psycopg2.errors.SyntaxError:
                return 0


def output_post(count):
    if connect:
        with connect.cursor() as cur:
            cur.execute(f'select question from questions order by id_sort desc offset {count} limit 1')
            return cur.fetchone()[0]


if __name__ == '__main__':
    if connect:
        connect.close()
