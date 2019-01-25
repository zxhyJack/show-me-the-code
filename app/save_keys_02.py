# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
import psycopg2
from psycopg2.extras import RealDictCursor
from coupon import generate_verification


def get_db():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="mutou",
            user="mutou",
            password="123456")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    else:
        return conn


def close_db(conn):
    if conn is not None:
        conn.close()


if __name__ == '__main__':
    sql = 'insert into coupon (content) values(%s)'
    keys = generate_verification(200, 16)
    conn = get_db()
    cur = conn.cursor()
    for key in keys:
        cur.execute(sql, [key])
    # cur.executemany(sql,_keys)
    cur.close()
    conn.commit()
    close_db(conn)
